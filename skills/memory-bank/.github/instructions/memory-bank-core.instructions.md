---
applyTo: "**"
---

# Memory Bank Core

Use the memory bank as durable repository context. These rules apply when reading or maintaining one; they do not require initialization for unrelated tasks or minor cosmetic edits. The [memory-bank skill](../skills/memory-bank/SKILL.md) defines the workflow.

## Memory Bank Resolution

Resolve the bank to `<target-repository-root>/.memory-bank/`, not the current subdirectory or the location where the skill is installed. Use the explicit task target first, then Git repository ownership of the files being worked on. For a non-Git project, use its explicitly selected project root.

Each independent repository or worktree has its own bank. A package inside a monorepo uses the monorepo root bank by default. Do not combine banks from separate repositories, write into another checkout, or use a parent bank as authority for a nested repository. For multi-root tasks, resolve and update each affected bank separately. Read [workspace banks](../skills/memory-bank/references/workspace-banks.md) when ownership is ambiguous; clarify the target before writing if the available context does not resolve it.

## Read and Write Rules

- Read the existing bank and applicable repository instructions before updating it. For navigation, start with `codebase-map.md` and confirm paths against the filesystem. Load other documents and feature records only as needed.
- The current code establishes implemented behavior. Explicit requirements establish intended behavior. The bank records both and their gaps; stale bank text must not override code evidence or silently erase intended requirements.
- Include relevant working-tree changes and label uncommitted state. Preserve user-authored content and unrelated changes. Do not reset source code to fit the bank.
- Write only to the resolved bank for the requested maintenance scope. Do not follow a symlinked bank into another location; resolve the intended ownership before writing.
- Use root-relative path labels and document-relative Markdown links. Keep secrets and machine-specific configuration values out of the bank.
- Record verification date, revision when available, dirty state, and checked scope. Mark unknowns explicitly. Do not claim full verification after a partial update or claim tests ran when they did not.
- Create missing documents from the skill's templates, replacing guidance with repository facts. Existing documents are updated selectively, never overwritten by blank templates.

## Closed Structure

The bank root contains only these standard artifacts:

```text
.memory-bank/
├── app-description.md
├── architecture-decisions.md
├── changelog.md
├── codebase-map.md
├── patterns-and-conventions.md
├── requirements.md
├── retention.json
└── features/
```

Use [artifact formats](../skills/memory-bank/references/artifact-formats.md) for content and [templates](../skills/memory-bank/assets/templates/) for initialization. Keep task plans, feature-specific agent instructions, and transient notes inside `features/<feature-slug>/`. Do not create root-level scratch files, competing overview documents, or new root directories without an explicit schema extension request. Preserve and report pre-existing extra artifacts; this rule does not authorize their deletion. Additional useful sections within the standard documents are allowed.

## Maintenance

Refresh affected documents after significant structural changes or any behavior/expectation change, even when the code diff is small. Skip purely cosmetic edits and equivalent local tweaks. Repair moved paths and links, update runtime descriptions and capability gaps, preserve stable decision IDs, and avoid duplicate changelog entries on repeated runs.

Promote lasting feature decisions and requirements into the core bank before closure or expiry. Preserve the canonical spelling `patterns-and-conventions.md`; consolidate unique content from the older misspelling `pattersn-and-convetions.md` and repair its links.

Apply feature cleanup only under [feature retention](../skills/memory-bank/references/feature-retention.md). Default to retaining everything. A retention duration alone does not authorize background scheduling or enable cleanup-on-update. Core documents never expire with feature records.

## Missing or Incomplete Memory Banks

For an explicit initialize/update request, create the missing bank or fill missing standard artifacts using code evidence. Create `features/` without fabricating a feature. For a significant code task, initialize or repair the relevant context as part of the skill's maintenance scope, but do not let undocumented details become invented requirements.

For a lookup-only request, inspect the repository directly if no usable map exists; report the gap without automatically generating a full bank. Preserve existing documents in a partial bank and identify unchecked areas. If evidence is unavailable, write an explicit unknown with the reason. Missing or invalid retention metadata blocks deletion, not other documentation work.
