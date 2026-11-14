# Dev Memory Bank

Shared Memory Bank foundation for agents and frameworks that use `.memory_bank` as the authoritive source of project context and as the durable store for AI-generated artifacts.

## What's Included

- [Memory Bank Core Instructions](.github/instructions/memory-bank-core.md): Always on rules for bank resolution, artifact ownership, the closed structure, and maintenance.
- [Memory Bank skill](.github/skills/memory-bank/SKILL.md): Initializes, repairs, or refreshes single project and polyrepo banks (`initialize` or `refresh`) with on-demand references for artifact formats, workspace bank routing, and feature retention plus root artifact templates.

## When to Subscribe

Subscribe when your agent or framework reads `.memory_bank/app-description.md` or `.memory_bank/patterns-and-conventions` before acting, writes persistent artifacts under `.memory_bank/features`, or needs a reusable way to initialize a missing or incomplete bank.

## Design Intent

This framework holds only cross cutting Memory Bank capabilities, workflow-specific orchestration and artifact schemas stay with the workflow that owns them. Root files capture current truth, and the changelog keeps the latest 25 detailed rows and compresses older ones by month. Sub-agents write Memory Bank files only at paths that are orchestrator names or their own workflow skill or agent file defines. 

Single-project workspaces need no configuration. Polyrepo workspaces declare their banks in a `memoryBank` object in `<workspace-root>/workspace.json` outside every bank; agents read the shared bank first and the active repository bank second. Shared contacts, requirements, and decisions stay in the shared bank; repository patterns, decisions, requirements, and feature history stay local. Each fact has one owner and other banks linked to it.

## Feature Retention

Initialization or refresh creartes `.memory_bank/features/retention-policy.md` with `retentionDays` (30, 60, 90, custom or `never`), `updatedAt`, `lastRunAt`, and Keep Exceptions, the folders cleanup never touches. Cleanup runs at initialization or refresh, on request, and at workflow startup at mostonce every seven days. A folder status is the `status:` front-matter line of its spec, RCA, analysis, or requirements file, or else the status in a legacy workflow state file

| Status | Cleanup |
| --- | --- |
| `draft`, `approved` | Kept; listed as stale once older than `retentionDays` |
| `completed`, `waived` | Deleted whole, decisions file included,  once older than `retentionDays`, and its branch is gone locally and on the remote |
| `abondened` | Deleted only with per-folder approval |
| none (unmanaged) | Listed once older than `retentionDays`; deleted only with per folder approval |

Before anything is deleted, one review per bank lists each folder's manual ACs and Out-of-scope items that no test preserves, and a folder whose `Verify: auto` AC ids no longer appear in test names needs per folder approval. The user can keep folders as Keep Exceptions or consolidate their durable requirements into `.memory_bank/requirements.md` first. Empty folders are deleted without asking. After cleanup, the PR body and, in tracked repositories, the git history are the only record.

## Tracking Feature Folders

Tracking `memory_bank/features` in Git is optional per team. Every workflow behaves the same whether it is tracked or ignored. Teams that want specs in review track only specs and their companion documents, decisions, mock-ups, and stories with this allow list; the policy stays untracked, so its `retentionDays` and Keep Exceptions hold only in the clone or work tree that wrote them, and cleanup deletes a track edfolder only with per-folder approval. Replace ,do not append: git cannot re-include a file under a directory that an earlier rule ignores, so first remove any rule that ignores `.memory_bank` or `.memory_bank/features/` as a directory. Where `.memory_bank/` itself was ignored, put `.memory_bank /*` and `!.memory_bank/features/` above the list so the root files and `tmps/` stay ignored. The list does not untrack a `retention-policy.md`. Git already tracks untrack it with `git rm  --cached`, and have teammates move their copy aside before pulling that commit and back after it.

```gitignore
.memory_bank/features/*
!.memory_bank/features/*/
.memory_bank/features/*/*
!.memory_bank/features/*/*.spec.md
!.memory_bank/features/*/*.decisiions.md
!.memory_bank/features/*/*open-questions.md
!.memory_bank/features/*/*.architecture.md
!.memory_bank/features/*/*.test-spec.md
!.memory_bank/features/*/mockup/
!.memory_bank/features/*/*.stories.md
!.memory_bank/features/*/stories/
```

`evidence/` carries its own `.gitignore` containing `*`.