# Rust: local inspection

Establish the edition, minimum supported Rust version, feature flags, and configured rustfmt/compiler/Clippy settings. Use existing tooling and enabled rules. Do not enable entire pedantic or restriction groups to generate more findings; Clippy's restriction lints can conflict with one another.

## Collect compiler and Clippy diagnostics

Find the containing `Cargo.toml`, workspace membership, `rust-toolchain`/`rust-toolchain.toml`, Cargo configuration, and existing CI commands. When rustup manages the tools, first inspect `rustup toolchain list` and the selected installed toolchain's components with `rustup component list --installed --toolchain toolchain_name`; avoid invoking proxies that would fetch a missing pinned toolchain. Once availability is established, check versions in that context with `rustc --version`, `cargo --version`, and `cargo clippy --version`. If a pinned toolchain or component is missing, report that prerequisite rather than triggering installation.

From the applicable crate/workspace directory, with dependencies and lockfile already prepared, use:

```text
cargo check --locked --offline --message-format=json
cargo clippy --locked --offline --message-format=json
```

Select the containing package with `-p package_name` in a workspace, or supply `--manifest-path path/to/Cargo.toml` when needed. Retain project-required target, feature, and target-selection arguments. Do not add `--all-features`, `--all-targets`, or `--workspace` unless they match the intended check scope. `--locked --offline` prevents lockfile changes and dependency fetching; missing cached dependencies or a required lockfile update blocks that check without authorizing repair of the environment.

Read Cargo `compiler-message` records, preserving diagnostic codes/lint names, level, message, primary spans, and relevant child notes. Other JSON records are not findings. Output can include ordinary text on stderr, so retain both streams and the exit status. A suggested edit is evidence to inspect, not permission for cross-file autofixes or `cargo fix`.

`cargo check` skips final code generation and cannot prove a complete build succeeds; retain an existing build gate when applicable. Clippy adds local lint evidence but does not replace compiler checks or manual inspection. If Clippy is unavailable, run the available compiler check and explicitly leave lint coverage unverified. Compare the same commands and configuration after edits.

## Linting, formatting, and security

Prefer compiler lints, Clippy, and rustfmt from the installed toolchain. Alongside compiler/Clippy checks, run the containing crate's configured formatting check, typically:

```text
cargo fmt -- --check
```

Preserve package selection and formatting configuration; report target-file formatting findings separately from other files. In authorized cleanup, use a formatter invocation that writes only the selected file. Rustfmt may follow module declarations, so verify traversal before writing; if target-only scope cannot be guaranteed, apply the required local formatting manually. Avoid unscoped `cargo fmt` or `cargo clippy --fix` on a larger package/workspace.

Use existing security analyzers when configured and manually inspect unsafe-block invariants, FFI boundaries, unchecked input-derived operations, command/query construction, and exposed sensitive data where applicable. Rust's ownership checks and a passing Clippy run do not prove absence of application-level vulnerabilities. Do not introduce unsafe code, unchecked conversions, or ignored errors to remove a diagnostic.

## Focus within each body

- Inspect unused imports, bindings, assignments, unnecessary `mut`, redundant conversions, and needless borrowing. Keep names and intermediate values that clarify ownership or intent.
- Examine cloning and allocation: remove demonstrably redundant copies when a local use permits it, while preserving required independently owned values. Do not redesign signatures or lifetimes to avoid a clone.
- Trace `Result` and `Option` handling, discarded results, panic paths, and suppressions. Prefer evidence-backed local handling, but do not replace `unwrap`/`expect` with arbitrary defaults or change an API to propagate errors without authorization for broader work.
- Simplify redundant matches, branches, closures, and iterator expressions when readability and behavior improve. Do not convert every loop into an iterator chain.
- Inspect guards and other RAII resources for intended scope and release points. Treat changes to lock/resource lifetimes as semantic changes requiring evidence.

## Semantic traps

- Borrowing, moving, and cloning are distinct. A clone may intentionally preserve an owned value for a later use or independently owned result.
- Reordering expressions, replacing eager work with lazy work, or removing bindings can affect side effects and drop timing. Preserve them, especially around guards and custom `Drop` implementations.
- `?` and early returns may alter surrounding control flow and require a compatible result type. Do not add them as mechanical syntax cleanup.
- `unsafe` blocks require their actual safety invariants. Do not claim safety from compiling successfully or replace unsafe code with an unverified alternative.
- Public items and feature-gated code may have uses outside the selected compilation. Check minimal context before deleting apparently unused items.

## Documentation when needed

For worked cleanup and preservation decisions, see [unnecessary mutability](examples.md#remove-unnecessary-mutability-and-a-redundant-temporary) and [necessary independent ownership](examples.md#rust-necessary-independent-ownership).

- [Rust ownership](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html) for moves, copies, and cloning.
- [Rust Reference: destructors](https://doc.rust-lang.org/reference/destructors.html) for drop scope when simplifying lifetimes.
- [Clippy](https://doc.rust-lang.org/clippy/) for lint categories and configuration; use rules appropriate to the project's toolchain.
- [cargo check](https://doc.rust-lang.org/cargo/commands/cargo-check.html) for package selection, JSON diagnostics, offline/locked behavior, and check limitations.
- [Clippy usage](https://doc.rust-lang.org/clippy/usage.html) for invoking the analyzer with Cargo.
- [Cargo JSON messages](https://doc.rust-lang.org/cargo/reference/external-tools.html#json-messages) for diagnostic record structure.
- [Rustup overrides](https://rust-lang.github.io/rustup/overrides.html) for project-selected toolchains.
- [Rustfmt](https://github.com/rust-lang/rustfmt) for formatter configuration, check mode, and module traversal.
