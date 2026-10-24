---
atom_id: CA-R-1609
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Subject/Domain/Node
  - Subject/Domain/Node/Continuant/Scope Unit
  - Single Source of Truth
version: 11
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-R-1470
  - CA-R-1568
  - CA-R-1746
tier: 3
type: Rule
---
# Summary

Distinguish projected representations from represented Entities

## Scope

Representations inside a Projection and the Entities they represent.

## Claim

a representation inside a Projection **must** remain distinct from the Entity it represents.

- depicting an existing Artifact **or** Scope Unit does **not** create another authoritative Artifact **or** Scope Unit.
- a representation **may** identify a source Entity **or** a derived element admitted by the Projection specification; source identities **and** traceability remain governed by CA-R-1746.
- this boundary introduces no separate Projection Element Term, lifecycle, **or** independently maintained authority.

## Details
