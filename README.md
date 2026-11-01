# Personal agents and skills

A personal library of reusable AI agent definitions, skills, and project templates for use across code repositories.

## Structure

```text
personal-skills/
├── README.md
├── AGENTS.md
├── SOURCES.md    # Inspiration and attribution for adapted work
├── .github/
│   ├── instructions/ # Repository instruction files
│   └── skills/       # Skills packaged with GitHub instructions
├── agents/       # Reusable agent definitions
├── skills/       # One directory per skill
├── templates/    # Starter instructions for consuming repositories
├── scripts/     # Installation and maintenance helpers
└── .gitignore
```

## Conventions

- Use lowercase, hyphenated names for agents and skills.
- Store agent definitions in `agents/<agent-name>.md`.
- Store each skill in `skills/<skill-name>/SKILL.md` or `.github/skills/<skill-name>/SKILL.md`, following its package layout. Keep one canonical definition per skill.
- Add `scripts/`, `references/`, and `assets/` within a skill only when needed.
- Keep reusable instructions here and project-specific context in the consuming repository.
- Never commit credentials, private keys, or local environment settings.

## Using this library

For now, copy selected definitions into the locations expected by your AI tool. Review and adapt them to the consuming project. Tool-specific paths and formats will be documented as support is added.

`scripts/install.sh` is a placeholder. It does not install or link anything yet. Once target tools are chosen, it can support linking selected definitions without overwriting existing project instructions.

See [Memory Bank](.github/skills/memory-bank/README.md) for the available memory-bank skill, its templates, design intent, and feature retention policy.

## Inspiration and sources

This library draws inspiration from other agent and skill repositories. See [Sources and inspiration](SOURCES.md) for the reference list and how to document skills or agents copied and personalized here.

## Next steps

1. Choose the AI tools this library will support.
2. Add the first agent definitions and skills.
3. Add project templates and implement installation for those tools.
