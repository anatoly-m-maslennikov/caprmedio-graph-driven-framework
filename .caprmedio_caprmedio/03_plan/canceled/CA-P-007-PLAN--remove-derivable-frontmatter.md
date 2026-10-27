---
artifact_subtype: change_plan
priority: medium
version: 3
updated_at: 2026-10-24 06:26:31 +0400
content_role: Plan
type: Plan
tier: 3
status: Canceled
author: Anatoly Maslennikov
current_scope_unit: caprmedio
atom_id: CA-P-007
---

# Remove derivable frontmatter

1. [ ] Ditch the default priority (`medium`).
2. [x] Ditch types in frontmatter; they are already in the filename.
3. [x] Consider deleting `scope_path` from frontmatter; it can also be derived from where the file sits.
