# Document structure

Resolve the target root using [workspace banks](workspace-banks.md), then create this bank there:

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
    └── <feature-slug>/
        ├── feature.md
        └── AGENTS.md
```

Create individual feature folders only when there is a feature to track. If Git needs to retain an initially empty `features/`, use `.gitkeep` and remove it when the first feature is added. See the feature artifact format below and [feature retention](feature-retention.md) for policy and cleanup rules.

The root structure is closed: do not add root files or directories beyond those listed without an explicit schema extension request. Preserve and report existing extras; do not delete them merely to conform. Additional feature-specific Markdown and agent files belong within the relevant feature folder.

## Templates

Initialize missing core artifacts from the same-named files in [assets/templates](../assets/templates/). Fill instructional comments and `{{...}}` tokens with evidence from the target repository, remove the comments, and mark unknowns explicitly. Do not overwrite existing documents with templates.

The template directory's `feature/` is a source template only: instantiate its `feature.md` and `AGENTS.md` inside `features/<feature-slug>/` when tracking actual feature work. Do not copy a directory literally named `feature/` into the bank root. The `retention.json` template is valid as-is and retains everything by default.

## app-description.md

Required sections:

- Overview
- Purpose
- Technical Stack
- Architecture Overview
- Project Structure
- Key Components
- Runtime Behavior Today
- Getting Started: Prerequisites, Run Locally, Run Tests
- External Dependencies

Summarize the major runtime flows, operational dependencies, and component responsibilities. Link to the detailed codebase map. Distinguish commands found in configuration from commands actually executed. For non-application repositories, describe their real purpose and workflow rather than inventing servers or runtime layers.

## codebase-map.md

This is the navigation entry point for agents looking for a file or folder.

Include:

- **Snapshot and coverage:** inspected revision, verification date, dirty state, scope, and excluded generated/vendor/cache paths.
- **Topology:** an annotated directory tree for first-party areas and a table of path, responsibility, and key entry points. Cover every first-party top-level area; expand significant modules and organize large maps into linked sections within this file.
- **Relationships:** dependency direction and runtime/data flow among components, grounded in imports, wiring, routes, or configuration. Label uncertain edges.
- **Task-to-path index:** where to change concrete capabilities, add routes, modify data models, configure builds, and find tests, using the repository's actual concepts.
- **Cross-cutting locations:** tests, configuration, migrations, scripts, shared types, documentation, and agent instructions where present.

Resolve links relative to the Markdown document, while displaying root-relative paths. Update incoming links and task lookups after moves or deletions. A map may group files by responsibility; it must not imply that a partial inventory covers every file. Search the current filesystem when a lookup is missing.

## architecture-decisions.md

Maintain an architecture decision log with columns **ID**, **Date**, **Decision**, **Status**, and **Notes**. Use stable IDs such as `ADR-001`. Useful statuses are proposed, accepted, superseded, deprecated, and unconfirmed.

Notes should capture supported rationale, tradeoffs, evidence, and replacement IDs. Use the actual decision date when known; otherwise label the date as the observation date. A structure discovered in code can be documented as an observation without fabricating a historical decision.

## changelog.md

Include **Recent Changes** and **Compressed History**. For each meaningful entry record the date, behavior or structural change, affected areas, and feature/PR/commit link when available.

When older entries overwhelm current context, compress them into dated summaries preserving behavior changes, breaking changes, migrations, and decision links. Do not delete unique durable context while compressing. There is no arbitrary changelog expiry tied to feature retention.

## patterns-and-conventions.md

Required sections:

- Naming Conventions
- Code Organization: Layering Pattern, Where Things Live
- Patterns in Use
- Testing Conventions
- API and Middleware Conventions
- Repository Conventions Worth Preserving

Cite representative files or symbols. Separate widespread patterns from one-off exceptions and recommendations. If the repository has no API or middleware, say so. Do not prescribe a new architecture while documenting the existing one.

## requirements.md

Required sections:

- Functional Requirements
- Current Capability Notes
- Security
- Quality Requirements
- Technical Constraints
- Business/Platform Constraints

For requirements, identify source and status (implemented, partial, planned, or unknown), and link to implementation or validation evidence when available. Keep observed capabilities distinct from promises or acceptance criteria. Record unknown business constraints explicitly. Security claims need evidence; absence of a discovered control is not proof that none exists.

## Updating an existing bank

Preserve meaningful sections beyond this schema. Consolidate duplicate content with links, retain valid historical records, and correct stale statements. Populate missing sections from evidence rather than filling them with generic project advice. Never label an entire bank current after verifying only a feature-sized subset.

## Feature artifacts

Use `.memory-bank/features/<feature-slug>/` for a substantive feature, branch, or PR. Reuse an existing record for the same work across branch renames or PR creation; do not create duplicates for every invocation. Use a filesystem-safe lowercase hyphenated slug, not a raw branch name containing slashes. Resolve collisions with a ticket or PR identifier.

Create `feature.md` with YAML frontmatter:

```yaml
---
name: account-export
status: active
created: 2026-11-01
last_activity: 2026-11-01
closed: null
retain: false
branches: []
pull_requests: []
---
```

Dates use ISO `YYYY-MM-DD` in the user's timezone. Allowed statuses: `active`, `paused`, `completed`, `abandoned`. `closed` is required for completed or abandoned features. Only change `last_activity` for substantive feature work, changed scope, decisions, or outcomes; a bank scan, formatting edit, or cleanup preview is not activity.

The body records purpose, scope, expected behavior/acceptance criteria, affected paths, decisions, progress, verification, and remaining work. Distinguish planned work from implemented behavior. Add `plan.md`, `notes.md`, or other Markdown artifacts only when they add useful detail.

Create a feature-local `AGENTS.md` containing feature-specific context, constraints, relevant paths, and validation expectations. It governs only its directory under normal agent-file scoping. Link it from `feature.md` and tell the working agent to read it explicitly for code work elsewhere; do not claim it automatically governs the feature's source files. Add other agent definitions only when the feature needs them.

Keep branch and PR links when known. Do not infer completion just because a branch is missing or a PR was merged; verify outstanding scope and record the outcome. On reopening, set `status: active`, clear `closed`, and update `last_activity` for the resumed work.
