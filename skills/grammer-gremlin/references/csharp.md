# C#: local inspection

Establish the project's language version, target framework, nullable context, `.editorconfig`, and enabled analyzers. Their configured rules govern diagnostics; do not upgrade language features as part of cleanup.

## Collect compiler and analyzer diagnostics

Find the containing `.csproj` and relevant `global.json`, shared build properties/targets, analyzer configuration, and existing CI command. Confirm the installed .NET SDK selected in that project context with `dotnet --version`; preserve its target framework and configuration. Do not substitute a standalone file build for an existing project.

For a project with dependencies already restored, a baseline and post-cleanup template is:

```text
dotnet build path/to/App.csproj --no-restore --no-incremental
```

Replace the example path and retain project-required arguments such as `--configuration` or `--framework`. `--no-restore` avoids implicit dependency restore; `--no-incremental` requests rebuilding rather than relying on up-to-date outputs. Missing restore assets, SDKs, workloads, or incompatible platforms are prerequisite failures, not code smells to fix in the selected file.

Capture compiler diagnostics (often `CS...`) and enabled analyzer diagnostics (such as `CA...`, `IDE...`, or third-party rule IDs), with their actual configured severity and locations. Building does not guarantee every IDE suggestion or style rule is enabled on build. Respect existing analyzer settings instead of enabling additional categories or changing warning severity to increase coverage. Attribute diagnostics from other projects separately.

If the file is compiled under several configurations/frameworks, use the relevant existing checks and state which were covered. A pass for one configuration does not establish cleanliness for all of them. Rerun the same build after edits and compare diagnostics using the core skill's evidence rules.

## Focus within each body

- Inspect unused usings and locals, dead stores, shadowing, redundant casts, and misleading local names. Retain initializer side effects and externally required members or attributes.
- Trace nullable values to dereferences. Prefer an evidence-backed guard or corrected local flow over the null-forgiving operator; do not change public nullability contracts merely to silence warnings.
- Inspect disposable resources for ownership, all exit paths, and the intended disposal point. Consider `using` or `await using` only when the resource's lifetime and ownership support it.
- Inspect asynchronous calls for unobserved work, blocking waits, and incorrect exception handling. Preserve method signatures and intended execution order; flag repairs needing an API change rather than spreading them across callers.
- Check catch blocks for swallowed errors, unnecessary wrappers, and misleading rethrows. Preserve exception information and documented recovery behavior.
- Inspect repeated enumeration, repeated expressions, nested branches, and redundant temporaries. Simplify locally only after establishing evaluation cost, side effects, and readability benefit.

## Semantic traps

- Converting a scoped `using` block to a declaration can extend the resource lifetime. Preserve the disposal boundary, including on return and exception paths.
- Rewriting LINQ or materializing an enumerable can change when and how often work runs. Treat enumeration timing, ordering, and exceptions as behavior to preserve.
- A property access or overloaded operator need not be a pure computation. Do not consolidate evaluations without checking their semantics.
- Public members and reflection/framework entry points can be used without ordinary call sites. Do not delete them based on file-local usage alone.
- Choices such as `var`, expression bodies, and pattern syntax follow configured conventions and clarity; they are not universal defects in either form.

## Documentation when needed

For a worked preservation decision, see [intentional disposal boundary](examples.md#c-intentional-disposal-boundary).

- [Microsoft: using statement and declaration](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/using) for disposal semantics and scope. Use documentation appropriate to the project's language version.
- [dotnet build](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-build) for build, restore, and incremental options.
- [.NET code analysis](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview) for compiler/analyzer distinctions and configured rule coverage.
