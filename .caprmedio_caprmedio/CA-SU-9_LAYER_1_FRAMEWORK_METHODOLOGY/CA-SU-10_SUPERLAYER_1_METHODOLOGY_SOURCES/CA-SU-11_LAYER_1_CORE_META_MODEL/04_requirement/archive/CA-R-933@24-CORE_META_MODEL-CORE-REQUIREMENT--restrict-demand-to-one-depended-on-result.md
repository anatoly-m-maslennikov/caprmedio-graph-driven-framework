---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Demand'
  depends_on:
  - Consumer Goal
  - Producer Result
version: 24
updated_at: 2026-10-24 02:14:24 +0400
relations:
  child_of:
  - CA-R-932
atom_id: CA-R-933@24
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
