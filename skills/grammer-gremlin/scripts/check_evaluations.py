#!/usr/bin/env python3
"""Check fixture behavior before/after isolated skill evaluation; install nothing."""

import argparse
import os
from pathlib import Path
import runpy
import shutil
import subprocess
import tempfile


def check_python(root):
    cleanup = runpy.run_path(str(root / "python/cleanup.py"))
    clean = runpy.run_path(str(root / "python/clean.py"))
    for value in (False, None, 0, 1, "yes", [], [1], True):
        assert cleanup["is_enabled"](value) is (value is True), repr(value)
    calls = []
    assert cleanup["invoke"](lambda: calls.append("called")) is None
    assert calls == ["called"]

    def fail():
        raise ValueError("callback failure")

    try:
        cleanup["invoke"](fail)
    except ValueError as error:
        assert str(error) == "callback failure"
    else:
        raise AssertionError("Callback error was swallowed")
    for value in (None, False, 0, "", [], "name"):
        assert clean["select_label"](value) == (value or "fallback")
    sentinel = object()
    assert clean["wire_value"](l=sentinel) is sentinel
    print("PASS Python behavior (no linter was run)", flush=True)


def run(command, cwd, env=None):
    subprocess.run(command, cwd=cwd, env=env, check=True, timeout=60)


def check_go(root, work):
    tool = shutil.which("go")
    if tool is None:
        print("SKIP Go: toolchain unavailable", flush=True)
        return
    work.mkdir()
    for name in ("cleanup.go", "clean.go"):
        shutil.copyfile(root / "go" / name, work / name)
    (work / "behavior_test.go").write_text('''package sample

import "testing"

func TestPositive(t *testing.T) {
    for _, value := range []int{-2, 0, 3} {
        if Positive(value) != (value > 0) { t.Fatalf("input %d", value) }
    }
}

func TestCapture(t *testing.T) {
    var got []int
    RecordBeforeAndAfter(func(value int) { got = append(got, value) }, 7)
    if len(got) != 2 || got[0] != 8 || got[1] != 7 { t.Fatal(got) }
}
''')
    env = dict(os.environ, GO111MODULE="off", GOTOOLCHAIN="local",
               GOPROXY="off", GOSUMDB="off", GOCACHE=str(work / "cache"))
    run([tool, "test", "-vet=off", "."], work, env)
    run([tool, "vet", "."], work, env)
    print("PASS Go behavior and vet", flush=True)


def check_rust(root, work):
    tool = shutil.which("rustc")
    if tool is None:
        print("SKIP Rust: toolchain unavailable", flush=True)
        return
    work.mkdir()
    source = (root / "rust/cleanup.rs").read_text()
    source += "\n" + (root / "rust/clean.rs").read_text()
    source += '''
#[test]
fn behavior() {
    assert!(!nonempty(""));
    assert!(nonempty("hello"));
    assert_eq!(owned_length(String::from("")), 0);
    assert_eq!(owned_length(String::from("é")), 2);
    let (mut left, right) = duplicate_owned(String::from("hello"));
    left.push('!');
    assert_eq!(left, "hello!");
    assert_eq!(right, "hello");
}
'''
    (work / "behavior.rs").write_text(source)
    binary = work / "behavior"
    run([tool, "--edition=2021", "--test", "behavior.rs", "-o", str(binary)], work)
    run([str(binary)], work)
    print("PASS Rust behavior (inspect compiler warnings; Clippy was not run)", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures", type=Path,
                        default=Path(__file__).resolve().parents[1] / "evaluations")
    args = parser.parse_args()
    root = args.fixtures.resolve()
    check_python(root)
    with tempfile.TemporaryDirectory(prefix="grammer-gremlin-") as directory:
        work = Path(directory)
        check_go(root, work / "go")
        check_rust(root, work / "rust")


if __name__ == "__main__":
    main()
