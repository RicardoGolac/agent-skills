# Sources and inspiration

Repositories to revisit for skill and agent ideas, workflows, and ways to organize this library. Selected definitions may be copied here and personalized over time.

## Reference repositories

| Source | What to explore for this library |
| --- | --- |
| [Matt Pocock — skills](https://github.com/mattpocock/skills) | Engineering skills; a reference for writing and organizing a personal skill collection. |
| [Cursor — pstack](https://github.com/cursor/plugins/tree/main/pstack) | Agents and skills packaged together; a reference for organizing related workflows and supporting documentation. |
| [Addy Osmani — agent-skills](https://github.com/addyosmani/agent-skills) | Engineering workflows for coding agents; a source of skills to evaluate and personalize. |

These are starting points for this library's design and future imports. Listing a repository here does not mean its contents have been imported.

## Bringing a skill or agent into this library

1. Choose a specific skill or agent and identify the upstream commit being copied.
2. Review its instructions, supporting scripts, dependencies, and license before adapting it.
3. Copy the needed files into `skills/<skill-name>/` or `agents/`, preserving applicable license and copyright notices.
4. Personalize the workflow for how you work, keeping project-specific details in consuming repositories.
5. Record the source, upstream revision, and meaningful changes using the attribution format below.
6. Try the adapted definition on a representative task before relying on it across projects.

## Attribution for adapted definitions

For an imported skill, add `SOURCE.md` inside its directory. For a standalone agent, add a `Source` section to its Markdown file. Use this format:

```markdown
# Source

- Original: [Author/repository — skill or agent](https://github.com/OWNER/REPO/tree/COMMIT/PATH)
- Upstream revision: <full commit SHA>
- Imported on: <YYYY-MM-DD>
- License: <license name and location of preserved notices>
- Local changes: <what was personalized and why>
```

When combining multiple sources, record each one. For ideas that inspire an original definition without copied content, a short inspiration link is sufficient.

Upstream updates are reviewed and applied manually so local customizations stay intentional. Update the recorded revision and change notes when incorporating newer upstream work.

## Imported definitions

None yet. Add an entry here when a skill or agent is imported:

| Local definition | Upstream source | Attribution |
| --- | --- | --- |
