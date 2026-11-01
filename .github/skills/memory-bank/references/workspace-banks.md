# Workspace banks

## Resolve ownership before reading or writing

Resolve the repository targeted by the user's task, independently of the skill's installation directory. A bank always belongs at that repository's root as `.memory-bank/`.

| Context | Bank to use |
| --- | --- |
| Explicitly selected repository | Its root `.memory-bank/` |
| File inside a Git repository | The owning Git working-tree root's `.memory-bank/` |
| Monorepo package without its own Git root | The monorepo root bank; describe package ownership in its map |
| Nested independent repository or submodule | Its own root bank; the parent may record the relationship but not duplicate its internals |
| Git worktree | The current worktree root bank, reflecting that checkout and branch |
| Workspace with several independent repositories | A separate bank per affected repository |
| Non-Git project | The explicitly selected project root; record revision as unavailable |

Do not select a bank merely because it is the nearest directory named `.memory-bank` or because the shell started in a workspace container. Do not create a shared workspace-level bank outside the repositories by default. If neither the task nor the working context identifies the target, ask which root to use before mutations.

## Existing and misplaced banks

Inspect existing root-bank content first. Report nested package banks or legacy bank locations as a possible conflict; do not silently merge, move, or delete them. Respect an explicitly requested migration separately from normal refresh work. Preserve unique information when a migration is authorized.

Resolve real paths before writing. If `.memory-bank/` or a target path redirects outside the selected bank through a symlink, stop that write and clarify intended ownership. Do not overwrite a regular file named `.memory-bank` as though it were a directory.

## Reading across repositories

A task spanning repositories may read each relevant bank and source tree. Keep findings attributed to their owning repository and revision. Document cross-repository dependencies in each relevant architecture overview or map, using stable repository links where available. Do not embed machine-local absolute paths in shared documents.

Only write to repositories included in the task. An upstream dependency discovered during investigation does not automatically authorize editing its bank.

## Branches and worktrees

A checked-out bank is a snapshot of that checkout, not proof of another branch's current state. Verify the current source and dirty state before trusting it. Feature branch names and PR links are context within a record, not alternate bank roots.

Preserve records for the same feature across branch renames. When reconciling conflicts, preserve distinct decisions and work rather than selecting the bank with the newest timestamp. Do not check out other branches or mutate another worktree merely to refresh this bank.

## Partial coverage

Record which repository, packages, and sections were verified. For multi-repository work, report updated banks individually. If one repository is unavailable, report that gap and continue independently authorized updates elsewhere; do not mark the whole workspace current.
