# Feature lifecycle and retention

## Feature folders

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

## Retention configuration

Create `.memory-bank/retention.json` with this default:

```json
{
  "version": 1,
  "retention_days": "all",
  "cleanup_on_update": false,
  "exceptions": []
}
```

- `retention_days`: exactly `30`, `60`, `90`, or `"all"`. `"all"` preserves everything.
- `cleanup_on_update`: boolean. Enable only when the user requests automatic cleanup during bank updates. Otherwise cleanup requires an explicit cleanup request.
- `exceptions`: exact feature folder slugs to retain, for example `["account-export"]`. No wildcards or paths.
- Feature-level `retain: true` also preserves that feature regardless of the global policy.

A request to set 30/60/90-day retention changes the configuration; it does not by itself enable cleanup-on-update or schedule a background job. No background scheduler is installed by this skill. A request for a one-time cleanup may authorize deletion within that request's scope without changing future cleanup settings.

## Eligibility

Only completed or abandoned feature folders are candidates. Active and paused records never expire automatically.

For a closed feature, calculate age from the **later of `closed` and `last_activity`**, using calendar dates in the user's timezone. It becomes eligible when age is **at least** the configured number of days. Do not use filesystem modification time, commit time, or creation date as a substitute.

Preserve a feature when:

- The global policy is `"all"`, its slug is in `exceptions`, or `retain` is true.
- It is active/paused, associated with the currently checked-out branch, or known to have an open PR.
- Metadata is missing, malformed, internally inconsistent, has an unknown status, or uses future dates. Report the issue rather than guessing defaults.
- It contains uncommitted, untracked, or ignored local work. In Git repos, check all three categories, including staged changes. If local-work safety cannot be established, skip deletion and report why.
- Durable requirements or decisions have not been promoted to the core bank.

Validate the configuration as a whole before cleanup. Unsupported values or a missing policy block deletion; they must not silently turn into an aggressive default. Explicitly unknown PR status for a linked PR should block deletion until resolved; records with no PR do not require one.

## Cleanup procedure

1. Read the policy and direct child feature directories. Inspect metadata and relevant local state. Produce exact candidates and preservation reasons; a preview never mutates files.
2. If cleanup is neither explicitly requested nor enabled for updates, report the preview and stop cleanup. Continue any independently requested documentation work.
3. Before deletion, verify each candidate is an actual direct child of `.memory-bank/features/` in the selected repository, with no symlink at the memory-bank root, features directory, feature directory, or inside the candidate. Skip symlinks; never follow paths outside this subtree. Never delete shared bank documents.
4. Preserve durable context in core documents and repair links from retained documents to records being removed. Do not leave dangling links or claim Git history contains records that were never committed.
5. Recheck eligibility and working-tree state immediately before deleting each eligible directory. Delete only those exact directories, never a broad glob or the whole features folder.
6. Report deleted folders, skipped folders with reasons, and any failures. Record a brief cleanup summary in `changelog.md` when deletion occurred; do not copy whole expired feature contents back into the bank.

Do not repeatedly seek permission when the user has already authorized this cleanup or configured cleanup-on-update. Respect any narrower scope in the current request, such as preview-only or preserving a named feature.
