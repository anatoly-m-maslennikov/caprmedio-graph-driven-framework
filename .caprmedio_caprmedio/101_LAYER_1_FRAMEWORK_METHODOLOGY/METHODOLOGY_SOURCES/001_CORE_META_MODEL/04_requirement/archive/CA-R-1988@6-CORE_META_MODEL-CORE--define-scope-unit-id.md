---
atom_id: CA-R-1988@6
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit.ID
relations:
  child_of:
  - CA-R-1174
version: 6
updated_at: 2026-10-24 01:37:42 +0400
tier: 1
type: Definition
---
# Summary

Define Scope Unit.ID

## Scope

Scope Unit identifiers.

## Claim

Scope Unit.ID **means** the identifier of one Scope Unit, distinct from its Name, Label and Path.

## Details

The Operator accepted a separate Scope Unit ID, and Candidate #5 includes it as an inherited property of Scope Unit Types. Candidate #6 decision 22 defines Path from parentage. CA-R-962 and CA-R-970 govern Name and its uniqueness; they do not define ID. This draft adds no new storage field or rename procedure.
