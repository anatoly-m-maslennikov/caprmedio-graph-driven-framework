---
atom_id: "CA-R-1966@draft"
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: "Draft"
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Selection"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-17 23:25:50 +0000"
---
# Summary

Define Entity/Continuant/Selection

## Scope

Selections and named Selections.

## Claim

a Selection **means** criteria for choosing members. a named Selection gives those criteria a name; it does **not** create another Object or independent copies of the selected members.

## Details

Candidate #6 preserves Selection separately from Object and concrete named selections separately from abstract Core kinds. CA-R-1447 defines Owned Atoms and CA-R-1448 defines Targeting Atoms; they define particular selections, not the general kind. This draft adds no selector syntax or mandatory materialization.
