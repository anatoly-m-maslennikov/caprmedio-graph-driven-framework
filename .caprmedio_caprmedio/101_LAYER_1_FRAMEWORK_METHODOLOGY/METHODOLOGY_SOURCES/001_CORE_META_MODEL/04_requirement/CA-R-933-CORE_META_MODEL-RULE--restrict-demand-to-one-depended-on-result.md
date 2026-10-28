---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Demand'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
version: 29
updated_at: 2026-10-27 20:00:12 +0400
relations:
  child_of:
  - CA-R-932
atom_id: CA-R-933
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 5
type: Rule
---
# Summary
Restrict Demand to one depended-on result

## Scope

Demand Atoms.

## Claim

**every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Goal depends.

## Details
