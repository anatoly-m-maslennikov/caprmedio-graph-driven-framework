---
artifact_type: plan
artifact_subtype: change_plan
artifact_id: CAPRMADIO-PLAN-011
scope_path: layer:meta
priority: medium
version: 1
updated_at: 2026-08-17 19:36:01
---

# Remove derivable frontmatter

1. Ditch the default priority (`medium`).
2. Ditch types in frontmatter; they are already in the filename.
3. Consider deleting `scope_path` from frontmatter; it can also be derived from where the file sits.
