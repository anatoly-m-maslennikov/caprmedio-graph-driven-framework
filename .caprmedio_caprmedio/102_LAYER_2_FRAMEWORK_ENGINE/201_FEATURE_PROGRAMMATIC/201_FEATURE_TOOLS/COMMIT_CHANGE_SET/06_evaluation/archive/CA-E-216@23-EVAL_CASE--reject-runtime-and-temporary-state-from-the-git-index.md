---
subjects:
  governs: Subject/Graph Node/Engineering/Delivery/Git Commits
  depends_on: []
version: 23
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-R-805
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-216@23
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject runtime and temporary state from the Git index

## Claim checked

Repository-local runtime, temporary, **and** Git-internal state cannot enter a commit through the managed pre-commit boundary.

## Test case

**in** separate runs, force-stage one file below `.caprmedio_runtime` **and** one file below `.caprmedio_tmp`, **then** invoke `git-hook pre-commit`.

## Acceptance criteria

Each run returns one stable local-machine-path diagnostic **before** commit creation **and** leaves the staged Carrier, working tree, index, refs, Journal, governed source, runtime, **and** temporary state byte-identical.

## Failure disposition

Reject the delivery **if** the boundary succeeds, silently unstages **or** rewrites either file, mutates governed state, **or** reports the runtime file as an Atom.
