---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Rule
version: 36
updated_at: 2026-10-27 20:00:02 +0400
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

Projections and their authoritative sources.

## Claim

A Projection is a non-authoritative output produced from a declared selection of sources through a Workflow:

source of truth → Workflow → Projection.

A Projection is not edited directly. Changes are made in its authoritative sources, then the Projection is rebuilt through its Workflow. Its sources may include other Projections; represented facts remain traceable through them to the appropriate source of truth under CA-R-1470. Multiple views of the same facts do not create independent authority.

The declared selection identifies the sources actually used. A Projection need not consume every source kind, and its generation need not be byte-deterministic.

## Semantics

Implementation is not a Projection merely because it realizes RMED. Code, tests, prompts, configuration and documentation can be edited directly and can be authoritative for actual implementation. A generated view of Implementation is a Projection when changes belong in its sources and the view is rebuilt.

## Details

The Workflow defines how the selected sources produce the Projection. Carrier materialization remains separate from that derivation under CA-R-1460.
