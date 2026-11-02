---
atom_id: CA-R-1609@15
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Projection
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Term//Artifact
  - Subject/Graph Node
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Rule
version: 15
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
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
