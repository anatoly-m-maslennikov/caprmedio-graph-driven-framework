---
subjects:
  governs: Subject/Graph Node/Engineering/Storage
  depends_on: []
version: 23
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-R-804
  - CA-M-087
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-233
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
---
# Resolve an ordinary project file action

## Test case

Given a Git-eligible non-Atom project file, **when** `COMMIT_CONTEXT` resolves an add, update, move, move-and-update, **or** removal trigger, **then** it returns one valid file-subject context with an empty graph-source set **and** a deterministic logger-owned revision **without** requiring Markdown, frontmatter, **or** Atom relations.

## Sources

- [CA-R-804 — Gather provisional programmatic action context concurrently](../04_requirement/CA-R-804-COMMIT_CONTEXT-RULE--gather-provisional-programmatic-action-context-concurrently.md)
- [CA-M-087 — Process one project-path action](../../05_method/CA-M-087-TOOLS-ENG_DECISION--process-one-project-path-action.md)
