---
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/Scope Unit
  - Structural Entity
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/History/Journal
  - Single Source of Truth
version: 29
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
atom_id: CA-R-1746
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Projection Artifact form

## Scope

Projection Artifacts and the authoritative sources represented in their derived views.

## Claim

a Projection **means** a non-authoritative generated view derived from its declared selection of authoritative sources **or** other Projections. source authority follows Single Source of Truth under CA-R-1470. **every** represented fact retains traceability through **any** upstream Projections **to** its appropriate authoritative sources. a Projection's source specification governs its required behavior **without** making its derived contents authoritative. multiple Projections of the same source facts, further derived views, **and** the choice of generation mechanism do **not** create another independent authority for those facts.

the declared selection identifies the sources actually used; it does **not** require **every** Projection **to** consume **every** source kind **or** require generation **to** be byte-deterministic.

## Details

The production relation RMED → using O → I is a projection/derivation of governing intent during Implementation. This does not permanently classify every native Implementation Carrier as a non-authoritative view: native I can subsequently supply actual-state source facts under CA-R-1470. A generated view of I, including its dependency graph, has no independent authority for those source facts. Ordinary Projection Artifacts remain non-authoritative.
