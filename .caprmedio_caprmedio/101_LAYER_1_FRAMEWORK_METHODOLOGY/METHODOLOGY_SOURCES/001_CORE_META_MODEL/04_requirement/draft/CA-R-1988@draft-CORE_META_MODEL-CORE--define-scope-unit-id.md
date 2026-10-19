---
atom_id: "CA-R-1988@draft"
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: "Draft"
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/Scope Unit.ID"
relations:
  child_of:
  - CA-R-1174
version: 3
updated_at: "2026-10-19 11:43:10 +0000"
---
# Summary

Define Scope Unit.ID

## Scope

Scope Unit identifiers.

## Claim

Scope Unit.ID **means** the identifier of one Scope Unit, distinct from its Name, Label and Path.

## Details

The Operator accepted a separate Scope Unit ID, and Candidate #5 includes it as an inherited property of Scope Unit Types. Candidate #6 decision 22 defines Path from parentage. CA-R-962 and CA-R-970 govern Name and its uniqueness; they do not define ID. This draft adds no new storage field or rename procedure.
