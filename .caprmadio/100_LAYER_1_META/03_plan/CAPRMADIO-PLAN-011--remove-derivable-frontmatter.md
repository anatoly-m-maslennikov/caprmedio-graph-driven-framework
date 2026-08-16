---
artifact_type: plan
artifact_subtype: change_plan
artifact_id: CAPRMADIO-PLAN-011
scope_path: layer:meta
priority: medium
---

# Remove derivable frontmatter

1. Ditch the default priority (`medium`).
2. Ditch types in frontmatter; they are already in the filename.
3. Consider deleting `scope_path` from frontmatter; it can also be derived from where the file sits.
