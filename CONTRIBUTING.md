# Contributing to HorX

Use one shared `main` branch and short-lived task branches. Review each other's work.
Branch protection and collaborator permissions are not configured by this scaffold.

## Start a task

Run from your own local HorX repository with a clean working tree:

```bash
git status
git switch main
git pull --ff-only origin main
git switch -c feat/your-focused-task
```

Implement and run relevant tests, then review and stage only intended files:

```bash
git diff
# Replace the example with the files changed for your task.
git add path/to/changed-file
git diff --staged
git commit -m "feat(module): describe the change"
git push -u origin HEAD
```

Open a pull request against `main`. Record actual test commands/results and anything
not tested. Request another member's review. After approval and required checks,
squash merge and delete the task branch. Do not force-push `main`.

## Integrate current main

With all work committed and a clean working tree, from your task branch:

```bash
git fetch origin
git merge origin/main
```

Resolve conflicts with the other author, stage the resolved files, complete the merge,
rerun tests and push. Use `git merge --abort` to abandon an in-progress merge.

## Before sharing

- Youssef Ashraf and Ahmed Amr jointly own application frontend/backend changes.
- Yahya and Ahmed share Web scanner changes; Yahya and NourEldin share AD scanner changes.
- Use top-level `scanners/`, `frontend/` and `backend/`; do not nest scanners
  inside the application backend.
- Coordinate shared schemas, migrations, dependencies and configuration changes
  with the application pair; scanner semantics need the relevant scanner owner.
- No credentials, real directory exports, private evidence or sensitive reports in Git.
- `.gitignore` is a convenience, not a secret detector. Inspect the staged diff.
- Rotate accidentally exposed credentials; deleting a file does not erase history.
- Label synthetic fixtures. Never invent scanner results or claim unrun tests passed.
- Coverage and failed/skipped/inconclusive states must survive parsing and rendering.

Current scaffold check:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Add real module and integration tests as functionality arrives. A passing scaffold
check does not validate scanner security or detection accuracy.
