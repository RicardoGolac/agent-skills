# Repository instructions

This repository stores reusable personal AI agents and skills.

- Keep additions focused and portable across projects.
- Put agent definitions in `agents/`, skill packages in `skills/`, and project starter files in `templates/`. Memory Bank packages its deployable `.github/` layout inside `skills/memory-bank/`; keep that layout inside the package, not at this repository's root.
- Give each skill its own package directory with a `SKILL.md` at its installation location; add supporting folders only when needed.
- State an agent or skill's purpose, when to use it, and its expected output.
- Give each new skill or agent a unique, simple personal name alongside its descriptive role. Include the short name in its canonical identifier, display title, and discovery description so other agents can refer to it naturally. Preserve existing names unless a rename is requested.
- Keep project-specific paths, credentials, and machine-local configuration out of reusable definitions.
- Preserve existing user instructions when adding installation support; never silently overwrite destination files.
- Update the relevant README when changing usage or layout.
- When adapting external agents or skills, follow `SOURCES.md` for attribution and preserve applicable license and copyright notices.
- Validate changed scripts and examples with checks appropriate to the change.
- Do not add frameworks, dependencies, or automation until a concrete use requires them.

## Short names

- **Greg** means [greg-grammer-gremlin](skills/greg-grammer-gremlin/SKILL.md), the file-by-file code hygiene reviewer. Load that skill for requests to have Greg review, lint, or scrub code; use its canonical identifier/path when handing the task to another agent. The nickname does not imply a separate `$greg` command or an installed standalone agent.
