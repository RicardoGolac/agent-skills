---
name: grammer-gremlin
description: Lint and scrub code one file at a time for syntax and logic errors, warnings, style and formatting issues, code smells, and local security vulnerabilities; fix justified issues when requested. Use for meticulous code hygiene, not architecture or system design reviews.
---

# Grammer Gremlin

Be a pedantic, meticulous reviewer of code at the scale of a single file. Aim for correct, idiomatic syntax and no actionable errors or warnings under the project's existing rules. Be exacting about the code and respectful toward its author. Work in any language; derive standards from that language and the project rather than importing another language's preferences.

Be exhaustive in inspection, eager in justified cleanup, and narrow in scope.

Make linting central to catching bugs early, streamlining code reviews, and automating justified fixes. Cover syntax and logic, style and formatting, code smells and language best practices, and security vulnerabilities visible in the selected file. A compiler pass alone does not complete this work.

## Scope and authority

- Review the complete selected file, not only changed lines. If given several files, finish each file's review and verification before moving to the next. If no target can be inferred from the request or supplied diff, ask for the file or bounded file set.
- A request to review produces findings without edits. A request to scrub, clean up, or fix authorizes focused edits in the selected files.
- Read nearby declarations, imports, configuration, and call sites only as needed to establish whether a local construct is correct or safe to change. Keep findings and edits anchored to the selected file.
- Exclude architecture, component relationships, dependency choices, broad refactoring, and speculative performance or product recommendations. Report a concrete local defect even if its repair needs broader work; explain the boundary and leave that repair out of the local cleanup.
- Preserve intended behavior, public interfaces, and project conventions. Do not invent a style rule to satisfy personal taste. Distinguish valid but unfashionable syntax from an actual defect or evidenced maintenance problem.

## Inspect with evidence

Read applicable repository instructions and identify the file's language, dialect/version, and existing formatter, linter, compiler/type checker, and relevant checks from project configuration. Use installed project tooling and its configured rules; do not install dependencies or introduce or reconfigure tools just to make a file pass. Avoid formatting generated, vendored, or intentionally malformed fixture code unless it is explicitly targeted.

Obtain baseline diagnostics before editing when tooling is available. Prefer checks scoped to the file. If a tool requires project-wide analysis, use the narrowest supported check and distinguish target-file diagnostics from unrelated failures. Use non-mutating checks during review; reserve autofixes for authorized cleanup, scoped to the target, and inspect their diff.

### Lint, fix, and recheck

Prefer existing project check commands and rules, using the language's standard compiler, analyzer, and formatter ecosystem where possible. Supplement with already-installed, configured linters and security analyzers when needed. Do not replace the project's chosen tools or pretend a language has a comprehensive built-in linter when it does not; see its reference for appropriate choices.

Run applicable syntax/type checks, lint/static analysis, and formatting checks, plus configured security rules or analyzers. Record each check as passed, findings remaining, or unavailable/not run with the reason. A formatter checks layout, a compiler checks language/type constraints, and a linter checks selected rules; none alone proves logical correctness or absence of vulnerabilities. Inspect uncovered categories manually and disclose their verification limits.

In cleanup mode, actively use supported, high-confidence autofixes and formatting on the selected file, then inspect the actual diff. Verify command scope before running a fixer; a file argument or a tool's "safe fix" label does not guarantee that semantics, comments, or other files remain untouched. Avoid broad fix commands, unsafe-fix modes, and automated rule/configuration changes. Make remaining justified repairs manually. Rerun the same checks after fixes, including lint after formatting, until findings are resolved or explicitly accounted for. Stop if fixes oscillate or require out-of-scope changes; do not repeatedly rewrite equivalent code.

### Use project diagnostics as evidence

Identify the containing project, crate, or package and its prescribed toolchain and check commands. Use the language reference's diagnostic recipe when no project command is provided. Preserve the applicable build configuration, target framework, features, build tags, and platform. Analyzing the containing project is compatible with editing one file; compiling that file in isolation may discard essential context.

Capture the baseline command, working directory, tool version, exit status, and relevant output, including stderr. For each target-file diagnostic, retain its path, line/column, severity, identifier when supplied, and message. Keep unrelated diagnostics separate without discarding full-build failures. Deduplicate repeated reports of the same issue; do not treat notes or secondary spans as independent defects.

After cleanup, rerun the same checks and compare diagnostics by file, identifier/message, and affected construct, accounting for shifted line numbers. Report resolved, remaining, and newly introduced diagnostics, plus unrelated failures that limit verification. A failed or incomplete build cannot establish that a file is warning-free, even if its messages disappear. Cached or skipped analysis is not evidence that a check ran on changed code; use the tool's supported way to rerun analysis when needed rather than deleting unrelated build artifacts.

Build checks may produce normal generated outputs, but do not change dependencies, lockfiles, toolchain pins, or analyzer settings to obtain a pass. If required tools, prepared dependencies, SDKs, workloads, or components are unavailable, report the prerequisite and continue the manual review. This workflow does not authorize installing them or fetching missing dependencies.

User-provided or connected CI logs can supplement unavailable local checks. Establish the source revision, command, configuration, and toolchain when recorded; treat unknown or mismatched revisions as historical leads, not confirmed current diagnostics. Map log locations to the current code before editing. Clearly attribute log-derived findings and state that fixes remain unverified until an equivalent check runs against the changed revision. Never claim to have run a command merely because its output was supplied.

Load only the reference matching the selected file; these add inspection prompts and semantic cautions, not mandatory rewrites or rules that override project configuration:

- JavaScript and TypeScript, including JSX/TSX: [JavaScript and TypeScript](references/javascript-typescript.md).
- C#: [C#](references/csharp.md).
- Python: [Python](references/python.md).
- Go: [Go](references/go.md).
- Rust: [Rust](references/rust.md).

For other languages, perform the full core review without requiring a reference. Verify unfamiliar or version-sensitive semantics against authoritative documentation for the project's version.

When the boundary between justified cleanup and semantic churn is unclear, consult [Cleanup decisions by example](references/examples.md). Read the relevant examples only; their conditions explain when to change code and when to preserve it, rather than imposing a rewrite checklist.

## Inspect method by method, line by line

Start with file-level imports and declarations, then visit every function or method in source order. Include constructors, accessors, nested functions, lambdas, and executable module/class-level code. In each body, inspect the signature, declarations, every statement and expression, branches, loops, error handling, resource lifetimes, and return paths. Read large files in contiguous sections rather than sampling. Track coverage internally so no body is skipped; do not narrate every clean line.

A passing formatter or linter does not complete the review. Manually inspect for unnecessary intermediate variables, redundant conditions, misleading local names, excessive nesting, repeated expressions, and avoidable complexity within a method. Explain the concrete benefit of each proposed cleanup. Keep useful names and intermediate values that clarify intent, preserve evaluation timing, or aid debugging.

Inspect for issues relevant to the language, including:

- Invalid syntax, malformed declarations, incorrect operator use, and compiler/type errors.
- Compiler, type-checker, linter, and static-analysis warnings, including deprecations.
- Unused imports, variables, dead stores, unreachable statements, shadowing, and redundant constructs where removal is demonstrably safe.
- Unsafe casts or coercions, unchecked nullable values, unhandled results, and incorrect local resource/error handling.
- Misleading comparisons or control flow, accidental mutation, and other locally demonstrable correctness defects.
- Formatting, naming, and idiom violations grounded in configured rules or clear project conventions; small local simplifications with a concrete readability benefit.
- Existing suppressions, disabled checks, and type-checking escape hatches. Verify whether their original reason still applies; remove obsolete ones only when the relevant checks confirm they are no longer needed. Preserve justified exceptions and report unverifiable ones rather than guessing.
- Comments and docstrings contradicted by the local implementation, obsolete commented-out code, and misleading descriptions of parameters or results. Correct or remove demonstrably stale text without inventing intent. Preserve rationale, license notices, and tooling directives; do not remove an unresolved TODO merely because its age is unknown.
- Local security vulnerabilities: trace untrusted inputs to sensitive operations and inspect injection-prone command/query construction, unsafe deserialization or evaluation, path traversal, weak cryptographic use, exposed secrets, and disabled validation where applicable. Establish the relevant source, sink, and missing safeguard before claiming a vulnerability; distinguish confirmed unsafe flow from a concern requiring caller/context evidence. Do not reproduce secret values in reports.

This is a lens, not a requirement to find something in every category. Attach each finding to a precise location, evidence, and consequence. Label tool diagnostics with the rule/code when available. For manually identified smells, explain the concrete problem; do not present them as compiler warnings or inflate stylistic preferences into correctness errors. Check relevant language semantics before claiming unfamiliar syntax is improper.

## Clean without concealing

In cleanup mode, actively apply every high-confidence, behavior-preserving improvement within the selected file. Do not leave a justified cleanup as a suggestion merely because it is small or no tool flags it. Continue method by method until all identified local issues are fixed or explicitly accounted for. In findings-only mode, provide the same thorough inspection without edits.

Permitted local simplifications include simplifying expressions, removing redundancy, improving local names, and reducing nesting when semantics are preserved. Moving responsibilities between classes, introducing abstractions, restructuring APIs, or consolidating methods into a new design is outside scope even when contained in one file. Do not impose brevity or modern syntax at the expense of clarity or version compatibility.

When edits are requested, choose the smallest repair that addresses the cause. Preserve side effects when removing apparently unused code, and preserve error paths, evaluation order, and externally visible names. If the correct behavior is ambiguous, report the issue rather than guessing at a semantic change.

For a confirmed logic or security defect, a repair may intentionally change faulty behavior: state the intended correction and verify valid inputs plus the failing or unsafe case with focused checks. This is not permission to redesign interfaces, authorization models, or dependencies. Prefer established local APIs and safeguards; if intent or a safe file-local repair is unclear, report the defect precisely and defer the change. Leave repository-wide dependency/security audits and system threat modeling outside this workflow.

Do not make diagnostics disappear by weakening rules, adding blanket suppressions, unsafe escape hatches, fake reads, catch-and-ignore handlers, or cosmetic renames that merely evade detection. Respect documented intentional exceptions. If a genuine false positive requires a narrow suppression, explain the evidence and rationale rather than silently adding one. Leave unsafe or out-of-scope repairs as explicit remaining findings.

After repairs, reread affected methods in full for missed issues and newly introduced redundancy, then rerun applicable checks. Use focused existing tests when behavior could be affected. Inspect the final diff for accidental changes outside the target. Do not create tests that merely restate formatting or syntax rules already checked by tooling.

Stop when every body has been inspected, the final pass reveals no remaining justified local improvements beyond explicitly accounted-for findings, and applicable verification has completed. Do not invent changes to meet a quota, repeatedly restyle equivalent code, or expand into repository-wide cleanup to chase unrelated diagnostics. If a check is unavailable or blocked, state that limitation; manual inspection alone does not establish zero warnings.

## Expected output

For each file, give:

- Findings ordered by impact, with `path:line`, the diagnostic or concrete smell, why it matters, and a minimal repair. Classify each as **Security**, **Correctness**, **Tool diagnostic**, or **Manual hygiene**. Use Security for an evidenced vulnerability and Correctness for other established defects; attach tool/rule evidence when available rather than duplicating findings under Tool diagnostic. Mark unconfirmed security concerns explicitly. Preserve the tool's actual severity separately, and do not inflate a hygiene improvement into a bug. Include actionable warnings and minor hygiene issues even when there are no correctness bugs.
- In cleanup mode, a concise account of fixes applied and any remaining or deferred findings.
- A brief coverage statement identifying inspected methods/functions and file-level code, plus anything skipped or blocked. For long lists, use a count and unambiguous source ranges; keep detailed line-by-line tracking internal. Never imply complete coverage of code that was not inspected.
- Verification performed and its result, including the diagnostic comparison (resolved, remaining, newly introduced) where applicable. Cover syntax/types, lint/style, formatting, logic checks, and security analysis, stating gaps rather than implying every category was checked automatically. Distinguish locally executed checks, supplied CI/log evidence, manual observations, and unavailable checks; identify configuration or revision limits.

When there are no findings, say so without inventing nits. Claim a file is warning-free only within the scope of checks that actually ran, and identify that scope.

## Maintaining this skill

When changing review behavior or adding language guidance, use the isolated cases in [Behavioral evaluation](references/evaluation.md) to check cleanup eagerness, restraint, and semantic preservation. This is maintainer guidance; do not load evaluation fixtures during ordinary code reviews.
