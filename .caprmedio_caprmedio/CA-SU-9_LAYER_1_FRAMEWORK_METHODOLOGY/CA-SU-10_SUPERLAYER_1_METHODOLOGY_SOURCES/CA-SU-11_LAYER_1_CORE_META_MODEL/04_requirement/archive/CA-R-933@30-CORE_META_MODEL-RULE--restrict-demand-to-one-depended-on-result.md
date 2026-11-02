---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Demand'
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
version: 30
updated_at: 2026-10-29 07:17:21 +0400
relations:
  child_of:
  - CA-R-932
atom_id: CA-R-933@30
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
