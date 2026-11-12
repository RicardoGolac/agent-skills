# Go: local inspection

Establish the module's Go version, build tags, and configured formatting and analysis checks. Use the existing toolchain; analyze the containing package when required, keeping edits and reported findings anchored to the selected file.

## Collect build and vet diagnostics

Find the containing package, applicable `go.mod`/`go.work`, and existing CI commands. Set `GOTOOLCHAIN=local` in the check process before running even `go version`, so discovering the installed version does not fetch a project-requested toolchain. Preserve build tags, platform, cgo settings, and workspace context; do not compile only the selected `.go` file and thereby omit its sibling declarations.

From the module/workspace directory, with dependencies already prepared, use:

```text
go build -mod=readonly ./path/to/package
go vet -mod=readonly ./path/to/package
```

Replace the package path with the selected file's containing package (`.` when already there). Prefer that bounded package over `./...`. Follow existing vendor-mode commands where applicable rather than imposing `-mod=readonly` on a vendored build. For locally prepared checks that must not fetch tools or modules, set `GOTOOLCHAIN=local`, `GOPROXY=off`, and `GOSUMDB=off` in the command's process environment, without changing persistent Go configuration. Missing modules or a mismatched installed toolchain are verification blockers, not permission to download dependencies or rewrite module files.

Capture build errors and vet findings with package, file, line/column, and message. Do not invent a warning identifier when the tool provides none; preserve analyzer names when available. Vet analyzes suspicious constructs beyond compilation, and its findings require interpretation. A build pass alone is not a vet pass; a vet pass does not eliminate the need for manual cleanup inspection.

Use the project's existing test commands when behavior could be affected, including relevant test-only or tagged files. Report the actual coverage; `go build` does not establish that test files compile or execute correctly. Rerun the same bounded build and vet commands after cleanup and compare diagnostics.

## Linting, formatting, and security

Use the standard ecosystem first: `go vet` for analysis and `gofmt` for formatting, alongside the containing-package build. For the selected file:

```text
gofmt -l path/to/file.go
```

`gofmt -l` lists files needing formatting; successful process exit alone does not mean the file is formatted. In authorized cleanup, use `gofmt -w path/to/file.go`, inspect the diff, and rerun formatting and vet checks. Supplement with existing configured tools such as Staticcheck or a project linter when installed; do not introduce another lint stack.

Vet is not a complete security analyzer. Use the project's installed source-security checks when present and manually inspect command/query construction, unchecked paths, cryptographic misuse, and validation bypasses in the file. Distinguish actual unsafe input flow from intentional trusted inputs; dependency vulnerability scans do not replace this review.

## Focus within each body

- Inspect ignored errors, overwritten errors, shadowed bindings, unused assignments, and misleading names. A discarded error needs an established reason; do not invent recovery behavior or change a public signature to make it disappear.
- Check cleanup after successful acquisition, deferred calls, and context cancellation on all exit paths. Keep ownership and intended lifetimes explicit.
- Simplify redundant boolean returns, needless branches, and temporary values. Preserve useful named results and intermediate values that explain intent.
- Inspect formatting arguments, copies of values containing locks, and locally visible goroutine/channel misuse. Report lifecycle problems needing system context without redesigning concurrency.
- Review blank identifiers and suppression comments for their actual purpose, including interface assertions and intentionally ignored results. Do not remove them solely because they look unused.

## Semantic traps

- Deferred call arguments are evaluated when the defer executes; a closure may read variables later. Replacing one form with the other can change observed values and cleanup order.
- Nil and empty slices/maps may have different observable behavior. Do not normalize them merely for consistency.
- Copying a struct can copy synchronization state; a shorter assignment is not automatically safe. Similarly, a typed nil inside an interface is not necessarily a nil interface.
- Loop-variable capture depends on the applicable language version. Check the module's version before claiming a closure defect or adding a workaround.
- `go vet` diagnostics are evidence requiring interpretation, not proof that every flagged construct is wrong or every unflagged file is clean.

## Documentation when needed

For a worked preservation decision, see [intentional deferred argument capture](examples.md#go-intentional-deferred-argument-capture).

- [Effective Go](https://go.dev/doc/effective_go) for core idioms and defer semantics; it predates newer language features, so consult version-specific documentation for those.
- [Go specification](https://go.dev/ref/spec) for language semantics, including interfaces and loop variables.
- [go vet](https://pkg.go.dev/cmd/vet) for the installed toolchain's applicable checks.
- [Go command](https://pkg.go.dev/cmd/go) for package selection, build flags, module behavior, and environment settings.
- [gofmt](https://pkg.go.dev/cmd/gofmt) for formatting checks and file-scoped writes.
