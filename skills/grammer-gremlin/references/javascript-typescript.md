# JavaScript and TypeScript: local inspection

Use for JS/TS and JSX/TSX. Establish the runtime, language target, module mode, TypeScript options, and configured lint/format rules first. Apply the core method-by-method review; these prompts supplement it.

## Focus within each body

- Inspect unused bindings, dead assignments, shadowing, misleading local names, and redundant expressions. Remove an unused import only after checking whether loading its module has required side effects.
- Check equality, coercion, truthiness, defaulting, and optional access against the actual value domain. Simplify only after establishing which values must remain distinct.
- Inspect unhandled promises, missing asynchronous error handling, and callbacks whose returned promises are not consumed. Establish intended sequencing before repairing async flow; do not add concurrency as cleanup.
- Check mutation, aliasing, and callbacks that capture changing variables. Prefer a non-reassigned declaration when compatible with project rules, but do not mistake a constant binding for an immutable object.
- In TypeScript, inspect unjustified `any`, assertions, non-null assertions, and suppressions. Prefer an existing precise type or a sound local guard when supported by evidence. Avoid assertions that merely silence the checker or changes that force a public type redesign.
- Simplify nested branches, repeated property access, and temporary values only where doing so improves readability without changing calls, getter evaluation, or value capture.

## Semantic traps

- `value || fallback` and `value ?? fallback` treat falsy values differently. Do not substitute one without proving the intended handling of `0`, `false`, and empty strings. Optional access also changes which nullish inputs throw.
- Loose and strict equality are not interchangeable for all inputs. Treat an equality change as a behavior repair requiring evidence, not a formatting fix.
- Removing `await`, changing a callback to an arrow, or replacing a loop with an array method can affect error handling, binding, sequencing, and control flow. Verify the relevant semantics rather than applying a blanket modernization rule.
- Do not remove apparently unused exports or framework callbacks based solely on references within the file. Read the minimum external context needed to establish their role.

## Documentation when needed

For a worked preservation decision, see [intentional falsy fallback](examples.md#javascript-and-typescript-intentional-falsy-fallback); the shared examples also show a safe redundant-branch cleanup.

- [MDN: nullish coalescing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing) for defaulting semantics.
- [TypeScript: everyday types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html) for `any`, assertions, and null handling. Check compatibility with the project's compiler version.
