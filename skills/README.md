# Skills

Store each reusable skill in its own directory under `skills/`, following its package layout:

```text
<skill-name>/
├── SKILL.md
├── scripts/       # Optional executable helpers
├── references/    # Optional supporting documentation
└── assets/        # Optional templates and resources
```

`SKILL.md` should explain when to use the skill, its workflow, and expected results. Follow the target AI tool's required format. Create supporting directories only when they contain useful material.

Some packages include a deployable layout instead. Memory Bank keeps its instructions and skill assets inside `memory-bank/.github/` for reuse in other repositories.

## Available skills

| Skill | Purpose |
| --- | --- |
| [grammer-gremlin](grammer-gremlin/SKILL.md) | Lint one file at a time for syntax/logic errors, warnings, style/formatting issues, code smells, and local security vulnerabilities; apply focused cleanup when requested. Excludes architecture and system design. |
| [memory-bank](memory-bank/README.md) | Create and maintain a root `.memory-bank/` with current codebase navigation, architecture, requirements, conventions, changes, and feature records with configurable retention. Package: `skills/memory-bank/`; deployable layout: its nested `.github/`. |

## Grammer Gremlin

Copy `grammer-gremlin/` into your AI tool's skill directory (for Codex, `~/.codex/skills/grammer-gremlin/`), checking for an existing destination before copying and preserving any local instructions. The package includes Codex UI metadata in `agents/openai.yaml`; its canonical instructions live in `SKILL.md`.

Invoke with `$grammer-gremlin Review path/to/file` for findings only, or `$grammer-gremlin Scrub path/to/file` for focused fixes and verification. Multiple selected files are handled sequentially. Results include located findings, fixes when requested, remaining issues, and the scope and outcome of checks actually run.

The Gremlin inspects every method and statement, performs a manual pass even when tooling passes, and actively applies justified local improvements in cleanup mode. It checks existing suppressions and comment accuracy, rereads affected methods, and verifies the result before finishing. Reports distinguish correctness defects, tool diagnostics, and manual hygiene findings and identify inspection coverage and limitations.

Focused references for JavaScript/TypeScript, C#, Python, Go, and Rust are loaded only for matching files; other languages receive the same core review. References guide inspection and semantic preservation rather than imposing style rules or expanding into design changes. See [behavioral evaluation](grammer-gremlin/references/evaluation.md) for isolated cleanup and leave-alone cases and their standard-library verification script. Shell-specific guidance is not included.

[Cleanup decision examples](grammer-gremlin/references/examples.md) explain four justified changes, including a local injection repair, and five constructs to preserve, with reasons. Universal patterns are shared; language-specific examples cover distinct semantic traps rather than repeating every cleanup in each language.

The C#, Rust, and Go references include project-level compiler/analyzer command templates. The Gremlin captures a baseline, maps diagnostics to the selected file, and compares the same checks after cleanup while keeping edits local. Supplied CI logs can guide review when local tooling is unavailable, but fixes remain unverified until equivalent checks run on the changed revision. Missing toolchains or dependencies are reported rather than installed by this skill.

Linting drives an explicit check–fix–recheck cycle to catch bugs early and reduce review noise. Prefer language-standard analysis and formatting (Roslyn/dotnet format, go vet/gofmt, Clippy/rustfmt) plus the project's existing tools; JavaScript/TypeScript and Python references cover configured ecosystem linters such as ESLint and Ruff. Automatic fixes remain scoped and reviewed. Reports distinguish lint, formatting, logic, and security coverage, and never equate a clean lint run with proof that no vulnerabilities exist.
