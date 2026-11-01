# Document structure

Create this bank at the target repository root:

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

Create individual feature folders only when there is a feature to track. If Git needs to retain an initially empty `features/`, use `.gitkeep` and remove it when the first feature is added. Read `feature-lifecycle.md` for feature metadata, additional artifacts, and retention configuration.

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
- **Topology:** an annotated directory tree for first-party areas and a table of path, responsibility, and key entry points. Cover every first-party top-level area; expand significant modules and use linked per-directory maps if a single file becomes unwieldy.
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
