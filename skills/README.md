# Skills

Store each reusable skill in its own directory:

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
| [memory-bank](memory-bank/SKILL.md) | Create and maintain a root `.memory-bank/` with current codebase navigation, architecture, requirements, conventions, changes, and feature records with configurable retention. |
