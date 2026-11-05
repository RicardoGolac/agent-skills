# Python: local inspection

Establish the supported Python versions and configured formatter, linter, and type checker from project configuration. Avoid introducing syntax unavailable in supported versions or adding type annotations as an unrelated campaign.

## Focus within each body

- Inspect unused imports, dead assignments, shadowing of built-ins, misleading local names, redundant branches, and temporary values. Check import side effects and re-exports before removal.
- Inspect mutable defaults and mutations through aliases. Determine whether state is intentionally shared before changing allocation timing or argument handling.
- Check identity versus equality, truthiness, sentinel handling, and nullable values against the actual inputs. Distinguish an absent value from a valid empty or zero value where the contract requires it.
- Inspect bare or overly broad exception handlers, swallowed exceptions, and unnecessary try blocks. Narrow handling only when the intended recoverable failures are established.
- Check resource ownership and cleanup on exceptions and early returns. Consider context managers where equivalent acquisition and cleanup behavior is supported.
- Inspect iteration for unnecessary indexing, repeated work, mutation during traversal, and unreadable comprehensions. Choose the clearer form without converting every loop or intermediate variable into an expression.
- Inspect nested functions for captured changing values and asynchronous code for unawaited work. Repair only with evidence of intended value capture or execution order.

## Semantic traps

- Defaults are evaluated when the function is defined. Replacing a mutable default with a sentinel changes state sharing and may change handling of an explicitly passed sentinel value; establish the contract first.
- `if not value` and `if value is None` accept different sets of inputs. Identity is appropriate for a known singleton/sentinel, not a blanket replacement for equality.
- A context manager's exit method can affect exception propagation. Confirm equivalence before replacing manual cleanup with `with`.
- Generators and comprehensions can alter laziness, scope, evaluation order, and allocation. Avoid conversions justified only by shorter code.
- Attribute access and operators can execute user code. Do not remove or merge repeated evaluations without checking side effects; preserve decorators and externally used names.

## Documentation when needed

For a worked preservation decision, see [intentional singleton test](examples.md#python-intentional-singleton-test); the shared examples also show how to remove a dead binding while preserving its call.

- [Python tutorial: default arguments](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) for definition-time evaluation and shared defaults.
- [Python reference: with statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement) for context-manager behavior. Consult the documentation version matching the project.
