---
atom_id: CA-P-011
ref_id: CA-P-011
container:
  scope_unit: CA-SU-00
role: Plan
form: Plan
tier: 3
status: Done
version: 2
updated_at: 2026-10-24 06:26:31 +0400
artifact_subtype: change_plan
priority: medium
author: Anatoly Maslennikov
current_scope_unit: caprmedio
---

# Replace relates to with precise relations

1. `relates_to` is a very bad relation type: anything relates to anything.
2. Ditch `relates_to`.
3. Apply existing relation types or create new ones where needed.
