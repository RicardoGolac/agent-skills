# Repository instructions

This repository stores reusable personal AI agents and skills.

- Keep additions focused and portable across projects.
- Put agent definitions in `agents/`, skills in `skills/` or `.github/skills/` according to their existing package layout, and project starter files in `templates/`. Memory Bank's canonical package is `.github/skills/memory-bank/`; do not duplicate its skill definition at the former location.
- Give each skill its own directory containing `SKILL.md`; add supporting folders only when needed.
- State an agent or skill's purpose, when to use it, and its expected output.
- Keep project-specific paths, credentials, and machine-local configuration out of reusable definitions.
- Preserve existing user instructions when adding installation support; never silently overwrite destination files.
- Update the relevant README when changing usage or layout.
- When adapting external agents or skills, follow `SOURCES.md` for attribution and preserve applicable license and copyright notices.
- Validate changed scripts and examples with checks appropriate to the change.
- Do not add frameworks, dependencies, or automation until a concrete use requires them.
