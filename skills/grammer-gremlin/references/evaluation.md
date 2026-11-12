# Behavioral evaluation

Use when maintaining the skill, not during ordinary reviews. Fixtures are deliberately small raw inputs, not examples to automatically copy into user code. No new dependencies are required.

## Isolated procedure

1. Copy `evaluations/` to a temporary directory. Keep the originals unchanged.
2. Give an independent evaluator the skill path, the copied source files, and a realistic request: "Use $grammer-gremlin to scrub these files, one file at a time. Preserve behavior and public interfaces; verify what you can with installed tools." Provide only the applicable language reference, not this evaluation document, expected outcomes, or the verification script. Permit changes only to the copied source files and prohibit tool installation.
3. Inspect its report and actual diff against the acceptance criteria below. Run `python3 scripts/check_evaluations.py --fixtures /absolute/path/to/copied/evaluations` from the skill directory. The script checks runtime behavior using installed tools; it does not judge cleanup quality or replace a diff review.
4. On fresh copies, request findings-only review. Verify the evaluator reports located, categorized findings and coverage while leaving all inputs unchanged. Also scrub the already-clean files alone and verify no cosmetic churn or invented findings.

Unavailable toolchains must be reported as skipped, never passed. Do not install them just for this evaluation. For full Go/Rust verification, rerun where the corresponding toolchains are available. Syntax/runtime checks alone do not prove lint cleanliness.

## Acceptance criteria

| Case | Cleanup expectation | Behavior and restraint |
| --- | --- | --- |
| [Python cleanup](../evaluations/python/cleanup.py) | Remove the unused import and its attached suppression, simplify the redundant boolean branches, correct/remove the contradicted comment, and remove the unused callback-result binding. | Only the singleton `True` enables; `1`, nonempty text, false, and null remain disabled. The callback still runs once and its exception propagates. No guessed changes to the function contract. |
| [Python clean](../evaluations/python/clean.py) | Leave unchanged; do not invent a hygiene defect. | Preserve fallback behavior for all falsy values and the public keyword `l`. Preserve the documented, intentional naming suppression. |
| [Go cleanup](../evaluations/go/cleanup.go) | Simplify the redundant boolean branches even when `go vet` passes. | Negative and zero inputs remain false; positive inputs remain true. Do not change the exported API or introduce new helpers. |
| [Go clean](../evaluations/go/clean.go) | Leave unchanged. | Deferred argument capture preserves the original value: input 7 records 8, then 7. Do not introduce a closure that reads the updated variable. |
| [Rust cleanup](../evaluations/rust/cleanup.rs) | Remove unnecessary mutability, simplify redundant boolean branches, and remove the redundant owned-string clone. | Preserve empty/nonempty results and UTF-8 byte lengths; keep signatures unchanged. Do not silence warnings with attributes or dummy reads. |
| [Rust clean](../evaluations/rust/clean.rs) | Leave unchanged. | Both returned strings retain independent ownership and original contents. Do not remove a necessary clone or redesign the signature to borrow. |

Across cases, require inspection coverage for all bodies and file-level code, distinction between tool diagnostics and manual hygiene, concrete evidence for correctness claims, and honest verification limitations. Judge meaningful cleanup and behavioral invariants, not exact replacement text or heading matches. The Go cleanup case is the lint-passing/manual-cleanup case only when `go vet` actually runs successfully.

## Lint and security scenarios

When changing lint/security behavior, also evaluate these focused scenarios in temporary copies:

- Introduce formatting drift in the Go cleanup case. Require a non-writing `gofmt -l` baseline, a target-file formatting repair in cleanup mode, and clean formatting plus vet rechecks. Other files must remain unchanged. Findings-only mode must not write formatting changes.
- Use the raw SQLite function from [the security example](examples.md#repair-a-confirmed-injection-path-with-the-apis-safeguard), telling the evaluator only that the connection uses SQLite and the name comes from untrusted input. Withhold the corrected example and acceptance expectations. Require an evidenced Security finding and a file-local repair; independently verify normal matches, names containing quotes, and injection-shaped names using an in-memory database. Preserve the interface, avoid schema redesign, and do not claim automated security coverage when only manual inspection/runtime checks ran.
- Supply a file containing a sensitive API call whose inputs are demonstrably constant/trusted. Require investigation of the actual flow rather than an invented vulnerability or a blanket rule against the API.

For all scenarios, require reporting of available and unavailable syntax/type, lint/style, formatting, logic, and security checks. Missing optional linters must not trigger downloads, newly enabled rules, or replacement of the project's tools.

## Adding language coverage

Pair each new language reference with at least one justified-cleanup case and one already-clean or intentional-construct case. Add behavioral assertions to the checker where practical. Include semantic traps suggested by real usage rather than collecting synthetic edge cases without a concrete purpose.
