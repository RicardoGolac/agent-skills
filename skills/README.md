# Skills

Store each reusable skill in its own directory under `skills/` or `.github/skills/`, following its package layout:

```text
<skill-name>/
├── SKILL.md
├── scripts/       # Optional executable helpers
├── references/    # Optional supporting documentation
└── assets/        # Optional templates and resources
```

`SKILL.md` should explain when to use the skill, its workflow, and expected results. Follow the target AI tool's required format. Create supporting directories only when they contain useful material.

## Available skills

| Skill | Purpose |
| --- | --- |
| [memory-bank](../.github/skills/memory-bank/README.md) | Create and maintain a root `.memory-bank/` with current codebase navigation, architecture, requirements, conventions, changes, and feature records with configurable retention. Canonical package: `.github/skills/memory-bank/`. |
