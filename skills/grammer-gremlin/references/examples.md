# Cleanup decisions by example

Read when calibrating whether a local change is justified. These are decision examples, not mandatory rewrites or additional style rules. Apply them only when their stated conditions hold and cleanup is authorized. A review-only request still produces findings without edits.

Universal lessons need only one example; language-specific examples are useful where syntax hides a semantic difference. Do not duplicate every pattern for every language. Each supported language below has a preservation example; new examples should explain a distinct decision rather than grow a catalog of equivalent spellings.

## Changes to make

### Simplify redundant boolean branches

Before (JavaScript):

```javascript
function isPositive(value) {
  if (value > 0) {
    return true;
  } else {
    return false;
  }
}
```

After:

```javascript
function isPositive(value) {
  return value > 0;
}
```

**Why:** The comparison already produces the returned boolean. This removes unnecessary branching, evaluates the comparison once, and preserves its result. This is Manual hygiene unless an actual tool diagnostic supplies additional evidence. Do not generalize to returning an arbitrary truthy value where the function must return a boolean.

### Remove an unused result without removing its side effect

Before (Python):

```python
def invoke(callback):
    result = callback()
    return None
```

After:

```python
def invoke(callback):
    callback()
    return None
```

**Why:** Given that `result` is never used and releasing its returned value earlier has no relevant effect, the binding is unnecessary. The call still occurs once and exceptions still propagate. Deleting the whole assignment without retaining the call would be wrong. If a returned resource or finalizer makes lifetime significant, retain the binding or investigate first. Report a warning only if a checker actually reports one; otherwise classify the dead binding as Manual hygiene.

### Remove unnecessary mutability and a redundant temporary

Before (Rust):

```rust
pub fn byte_count(text: &str) -> usize {
    let mut count = text.len();
    count
}
```

After:

```rust
pub fn byte_count(text: &str) -> usize {
    text.len()
}
```

**Why:** The value is never reassigned, and the temporary adds no explanation beyond the method name. Returning the length directly preserves the byte count and public signature. If the compiler reports `unused_mut`, record that diagnostic and confirm its removal after the edit. Do not add `allow(unused_mut)` or a dummy mutation to hide it.

## Code to leave alone

### JavaScript and TypeScript: intentional falsy fallback

```javascript
function label(value) {
  // Empty text, zero, and false intentionally use the fallback too.
  return value || "fallback";
}
```

**Why:** Replacing `||` with `??` would retain zero, false, and empty text instead of falling back. Modern-looking syntax would change the documented contract. Preserve the expression unless the user requests that behavior change. See [nullish-coalescing semantics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing).

### Python: intentional singleton test

```python
def explicitly_enabled(value):
    """Only the True singleton enables this option."""
    return value is True
```

**Why:** `bool(value)` would accept nonempty strings and other truthy objects; `value == True` would also accept `1`. Neither is equivalent to this explicit contract. Do not replace a precise predicate merely because truthiness is a common idiom.

### C#: intentional disposal boundary

```csharp
static byte[] WriteThenRead(string path)
{
    using (var stream = System.IO.File.Create(path))
    {
        stream.WriteByte(42);
    }

    return System.IO.File.ReadAllBytes(path);
}
```

**Why:** The stream is disposed before the read. Replacing the block with a method-scoped `using var stream = ...` would keep it open during `ReadAllBytes`, changing resource lifetime and potentially preventing the read. Keep the explicit boundary; shorter syntax alone is not a benefit. See [using scope and disposal](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/using).

### Go: intentional deferred argument capture

```go
func RecordBeforeAndAfter(record func(int), value int) {
	defer record(value)
	value++
	record(value)
}
```

**Why:** With input 7, this records 8 and then 7. Replacing the defer with `defer func() { record(value) }()` would read the updated variable later and record 8 twice. Keep the direct deferred call. See [deferred argument evaluation](https://go.dev/doc/effective_go#defer).

### Rust: necessary independent ownership

```rust
pub fn duplicate_owned(value: String) -> (String, String) {
    (value.clone(), value)
}
```

**Why:** The contract requires two independently owned strings. The clone supplies the second value; removing it would attempt to move the same owned value twice. Changing the signature to return borrowed strings would redesign the API. Keep this clone while still inspecting other clones on their own merits. See [Rust moves and cloning](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html).

## When intent is missing

These preservation examples establish intent through documentation, signatures, or concrete behavior. Without that evidence, investigate the smallest relevant context rather than assuming either that the code is wrong or that every existing choice is intentional. Fix established defects; leave ambiguous semantic changes as precise findings. A justified, behavior-preserving improvement elsewhere in the method should still be applied.
