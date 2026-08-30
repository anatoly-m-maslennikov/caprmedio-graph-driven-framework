---
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 4
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-804
    - CA-M-087
  derived_from:
    - CA-A-057
---
# Resolve an ordinary project file action

Given a Git-eligible non-Atom project file, when `COMMIT_CONTEXT` resolves an add, update, move, move-and-update, or removal trigger, then it returns one valid file-subject context with an empty graph-source set and a deterministic logger-owned revision without requiring Markdown, frontmatter, or Atom relations.
