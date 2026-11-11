---
atom_id: CA-P-007
ref_id: CA-P-007
container:
  scope_unit: CA-SU-00
role: Plan
form: Plan
tier: 3
status: Canceled
version: 3
updated_at: 2026-10-24 06:26:31 +0400
artifact_subtype: change_plan
priority: medium
author: Anatoly Maslennikov
current_scope_unit: caprmedio
---

# Remove derivable frontmatter

1. [ ] Ditch the default priority (`medium`).
2. [x] Ditch types in frontmatter; they are already in the filename.
3. [x] Consider deleting `scope_path` from frontmatter; it can also be derived from where the file sits.
