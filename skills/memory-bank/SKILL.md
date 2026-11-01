---
name: memory-bank
description: Create or refresh a root .memory-bank with current architecture, behavior, requirements, codebase navigation, and feature records. Use after significant code or organization changes, any behavior or expectation change, or explicit memory-bank mapping, update, or retention requests. Skip cosmetic edits and minor internal tweaks with no behavior or structural impact.
---

# Memory Bank

Maintain durable, evidence-based repository context in `<repo-root>/.memory-bank/`. Create it when absent; reconcile it with the current checkout when present. Keep automatic skill selection enabled. This skill provides instructions when selected; it does not install a watcher, Git hook, or scheduled job.

## Decide the scope

- **Initialize:** inspect the repository and create the core documents, map, retention configuration, and `features/` directory described in [document structure](references/document-structure.md).
- **Refresh:** update affected documents after architecture, module ownership, folder layout, dependencies, APIs, runtime behavior, requirements, or developer workflow changes. A small code diff that changes behavior or expectations still qualifies. Pure formatting, spelling, or equivalent local refactors do not.
- **Map or locate:** create or reconcile `codebase-map.md`; use its task-to-path index to locate code, verifying the referenced path before relying on it. A lookup alone need not rewrite the whole bank.
- **Feature work:** maintain a feature folder for a substantive feature, branch, or PR. Read [feature lifecycle and retention](references/feature-lifecycle.md) before creating, closing, or pruning feature records.
- **Cleanup:** apply the configured feature retention policy using the lifecycle reference. Ordinary updates do not imply permission to delete records unless cleanup-on-update was explicitly enabled.

Do the requested mode without creating unrelated code changes or installing this skill globally. Do not create a memory bank in this skill library merely because the skill is being authored here.

## Establish evidence

1. Find the target repository root using its Git root or the explicitly supplied project root. In a monorepo, use that root unless the user explicitly selects a separate nested repository. Inspect applicable repository instructions and existing memory files before writing.
2. Check the current branch, HEAD, working-tree changes, and relevant file inventory. Include current uncommitted code in the snapshot and label it as such. Never reset or discard changes to obtain a clean snapshot.
3. Read entry points, package/build manifests, routing, configuration schemas, core modules, tests, and existing docs relevant to the task. Verify commands from repository files. Avoid secrets, dependency caches, generated output, and vendor code; note intentional map exclusions.
4. For incremental updates, use a known previous snapshot commit when available, plus staged, unstaged, and relevant untracked changes. Do not assume the last commit or default branch contains the whole change. If the baseline is missing or unavailable, inspect the current structure directly.
5. Separate **observed implementation**, **documented intent**, and **unknowns**. Code and tests establish current behavior; explicit specs or user decisions establish requirements. Preserve intended requirements when implementation falls short, recording the gap. Never invent architecture rationale, business rules, security guarantees, or test results.

## Maintain the bank

Read [document structure](references/document-structure.md) for the required files and sections. Create missing files with substantive repository-specific content; use “Unknown” or “Not applicable” with a short reason where evidence is unavailable. Preserve useful existing material and user-authored decisions.

- Treat `codebase-map.md` as the maintained source of truth for navigation, with actual code authoritative when they disagree. Repair stale paths instead of letting the map override filesystem evidence.
- Use root-relative paths and Markdown links to evidence. Prefer file paths and symbols over line numbers that quickly drift. Include entry points, component ownership, dependency direction, and task-to-path lookups, not just a directory tree.
- Keep current-state documents focused on today. Put historical rationale in decisions, changes in the changelog, and transient plans in feature folders. Cross-link instead of copying large sections.
- Record snapshot metadata on current-state documents: last verified date, inspected commit when available, dirty-checkout status, and scope/exclusions. Only advance a document's verification metadata after checking its contents; partial verification must identify the checked sections.
- Log a meaningful code or behavior change once. A repeated refresh with no new facts should not add changelog or decision entries. Do not manufacture code changes for documentation-only initialization.
- Keep stable decision IDs; supersede or deprecate previous decisions rather than silently replacing their history. Mark inferred rationale as unconfirmed, not accepted.
- When a feature changes durable behavior, promote its requirements, decisions, conventions, and navigation changes to the core bank before closing it. Feature deletion must not remove the only record of a lasting decision.

Use `patterns-and-conventions.md` as the canonical spelling. If the legacy `pattersn-and-convetions.md` exists, preserve its unique content, consolidate it into the canonical file, and repair links. Avoid maintaining two competing versions.

## Verify and report

Check that required sections exist, local links and mapped paths resolve, and the map reflects changed ownership and entry points. Review claims against the relevant code and tests. Run commands only when needed and authorized by the task; report unrun checks as unverified. For documentation-only work, link/path and consistency checks are usually sufficient.

For retention, report the policy, eligible folders, protected exceptions, and actual deletions separately. Never claim cleanup happened when only a preview was produced.

Finish with a concise account of created or updated documents, meaningful discoveries, verification performed, and unresolved gaps. Do not commit, push, or modify repository-wide agent configuration unless the surrounding task authorizes it.
