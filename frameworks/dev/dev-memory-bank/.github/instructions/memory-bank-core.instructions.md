---
name: Memory Bank Core
description: Shared Memory Bank read, write, structure, retention, and maintenance rules
applyTo: "**"
---

# Memory Bank Core Instructions

Treat `.memory_bank/` as the durable project context and handoff surface. Code is authoritative over a stale or conflicting bank; fix the bank as part of the work.

## Bank Resolution

- Check each declared workspace root's `workspace.json` for a `memoryBank` object; never search repository banks for a registry.
- With none, use the active workspace root's `.memory_bank/`. With exactly one, resolve banks with the memory bank skill's [workspace-banks.md](../skills/memory-bank/references/workspace-banks.md). With more, ask the user to choose.
- Read the shared bank first, then the active repository bank, which takes precedence only for repository-level facts.
- Keep one owner per fact: integration contacts, shared requirements, and cross-repository decisions in the shared bank; code patterns, local decisions, requirements, and feature history in the repository bank. Link to the owner by stable ID or path instead of copying, and update every affected bank in cross-repository work


## Read and Write Rules

- Before substantial work, read only the relevant root documents and active `.memory_bank/features/[work-item]` artifacts.
- Follow `patterns-and-conventions.md`; reuse relevant architecture decisions before structural changes.
- Reuse the active work item folder, preserve upstream artifacts, and update only artifacts the current workflow owns.
- Sub-agents write memory bank files only at paths their orchestrator names or their own workflow skill or agent file defines.
- Before completion, update affected artifacts with durable facts, decisions, outcomes, or pointers, or state that no update is required.

## Closed Structure

- The only root files are `app-description.md`, `requirements.md`, `patterns-and-conventions.md`, `architecture-decisions.md`, and `changelog.md`. A polyrepo registry belongs in the workspace root `workspace.json`, outside every bank.
- The only feature-area control file is `features/retention-policy.md`.
- Create feature artifacts only when a defined workflow owns their name and format. Ask before adding a new artifact type.
- Tracking `.memory_bank/features/` in Git is optional. It works the same whether it is tracked or ignored. Uncommitted retention changes under `.memory_bank/features/` ( deleted folders, policy edits) are for the user to commit, never an unrelated change that stops a step.
- Use `.memory_bank/temp/` only for disposable scratch work, never for secrets or to bypass the closed structure.

## Maintenance

- Keep root files current and concise. Revise stale content instead of accumulating history
- Log only completed material locally validated changes in `changelog.md`. Keep 25 detailed rows and compress older entries by month
- Run the Memory Bank skills `feature-retention.md` procedure at initialization or refresh (create or repair `features/retention-policy.md` first), when the user asks for feature cleanup, pruning, or retention review, and at workflow startup before writing feature artifacts when the policy's `lastRunAt` is missing or older than seven days.
- Do not store raw tool output transcripts, exhaustive file lists, or review chatter in durable artifacts. The one exception `<slug>.decisions.md` keeps the user's request and typed replies (answer, approvals, attestations and waivers) verbatim.

## Missing or Incomplete Memory Banks

For workflows that need durable artifacts or handoffs, initialize or repair the memory bank first with the [Memory Bank skill](../skills/memory-bank/SKILL.md). For lightweight work, state that you are proceeding without memory bank context