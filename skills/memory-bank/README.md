# Memory Bank

A reusable skill for keeping a repository's architecture, behavior, requirements, and navigation context current in a root `.memory-bank/` folder.

## What's included

| Package item | Purpose |
| --- | --- |
| [SKILL.md](.github/skills/memory-bank/SKILL.md) | Invocation criteria and initialize, refresh, map, feature, and cleanup workflows |
| [Core instructions](.github/instructions/memory-bank-core.instructions.md) | Repository rules for bank resolution, reads and writes, closed structure, maintenance, and missing banks |
| [Templates](.github/skills/memory-bank/assets/templates/) | Six core Markdown documents, retention configuration, and feature/agent templates |
| [Artifact formats](.github/skills/memory-bank/references/artifact-formats.md) | Required sections, evidence expectations, and feature metadata |
| [Feature retention](.github/skills/memory-bank/references/feature-retention.md) | Retention options, exceptions, eligibility, and cleanup procedure |
| [Workspace banks](.github/skills/memory-bank/references/workspace-banks.md) | Repository, monorepo, multi-root workspace, and worktree ownership |
| [Agent metadata](.github/skills/memory-bank/agents/openai.yaml) | Display name and default invocation prompt |

The generated bank contains:

```text
.memory-bank/
├── app-description.md             # Purpose, stack, architecture, runtime, setup
├── architecture-decisions.md      # Stable decision IDs, status, rationale
├── changelog.md                   # Recent changes and compressed history
├── codebase-map.md                # Topology, relationships, task-to-path index
├── patterns-and-conventions.md    # Naming, organization, tests, APIs, conventions
├── requirements.md               # Requirements, capabilities, constraints, gaps
├── retention.json                # Feature cleanup policy
└── features/
    └── <feature-slug>/
        ├── feature.md            # Scope, branch/PR context, progress, verification
        └── AGENTS.md             # Feature-specific agent context
```

Feature folders are created when needed. Supporting feature plans and notes stay inside their feature folder. The bank root is closed to the listed artifacts unless its schema is explicitly extended.

## When to use it

- Initialize a bank in a repository that has none, or repair an incomplete bank.
- Refresh context after meaningful architecture, dependency, module ownership, folder, API, or developer workflow changes.
- Record any change in behavior or expectations, even if the implementation diff is small.
- Build or refresh a topological codebase map, or locate implementation through an existing map.
- Track a substantive feature, branch, or PR and preserve its lasting decisions.
- Preview or perform feature cleanup under the configured retention policy.

Pure formatting, spelling corrections, and internal tweaks with equivalent behavior do not require a refresh. A lookup-only request can use the source tree directly if a bank is absent.

Example requests:

```text
Use $memory-bank to initialize this repository's memory bank.
Use $memory-bank to refresh the map and behavior docs after this module move.
Use $memory-bank to track the account-export feature and its acceptance criteria.
Use $memory-bank to set feature retention to 60 days, preserving account-export.
Use $memory-bank to preview expired feature records without deleting anything.
```

## Design intent

The bank gives agents a compact, durable starting point instead of repeatedly rediscovering the repository. The map is the maintained navigation source of truth; actual files and code resolve conflicts when the map is stale. Requirements describe intended behavior, and capability notes describe what is implemented today.

Updates are evidence-based and scoped to what changed. Verification metadata identifies the inspected revision, dirty state, date, and coverage. Unknowns stay explicit. Repeated refreshes should not produce duplicate decisions or change entries.

Core documents retain durable knowledge; feature folders hold transient work. Lasting decisions and requirements move into core documents before a feature expires. Each independent repository or worktree owns its bank, while packages normally share their monorepo root bank.

The skill is instructions and templates, not a daemon. Automatic selection depends on the host agent discovering the skill; no watcher, Git hook, scheduler, or global installation is created. Feature-local `AGENTS.md` files must be read explicitly when working on source outside their directory.

## Feature retention

The default retains everything:

```json
{
  "version": 1,
  "retention_days": "all",
  "cleanup_on_update": false,
  "exceptions": []
}
```

Choose `30`, `60`, `90`, or `"all"` for `retention_days`. Eligible closed features expire at the chosen age, measured from the later of closure or last substantive activity. Active and paused features are preserved.

Add exact feature slugs to `exceptions`, or set `retain: true` in a feature's metadata, to keep individual records indefinitely. Local work, invalid metadata, current-branch work, and unresolved/open PR state also prevent deletion. Core bank documents do not expire.

Setting a duration only configures eligibility. Cleanup occurs on an explicit cleanup request or during updates after `cleanup_on_update` has been explicitly enabled. Preview-only requests never delete anything. See [feature retention](.github/skills/memory-bank/references/feature-retention.md) for the complete rules.

## Package location and reuse

The reusable package lives at `skills/memory-bank/` in this library:

```text
skills/memory-bank/
├── README.md
└── .github/
    ├── instructions/
    │   └── memory-bank-core.instructions.md
    └── skills/
        └── memory-bank/
            ├── SKILL.md
            ├── agents/
            ├── assets/templates/
            └── references/
```

To use the complete GitHub layout in another repository, copy this package's `.github/` contents into that repository's `.github/`, merging with existing files without overwriting unrelated instructions. Internal links between the core instructions and the skill are preserved. The generated `.memory-bank/` belongs at the consuming repository's root.

For an agent that uses a different skill location, copy the complete inner `.github/skills/memory-bank/` folder into that location. Adapt any companion instruction links and the host's instruction-loading configuration as needed.

Copy templates only when initializing missing bank artifacts, populate them from the target repository, and leave existing documents intact. The `assets/templates/feature/` directory is instantiated as `features/<feature-slug>/`; it is not copied into the bank root.
