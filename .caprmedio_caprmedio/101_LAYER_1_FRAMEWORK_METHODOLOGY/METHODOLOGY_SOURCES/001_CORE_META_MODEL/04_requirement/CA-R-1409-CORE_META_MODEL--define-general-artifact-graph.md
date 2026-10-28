---
subjects:
  governs: Subject
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Carrier
  - Subject
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
version: 24
updated_at: 2026-10-27 19:59:54 +0400
relations: {}
atom_id: CA-R-1409
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define General Artifact Graph

## Scope

the General Artifact Graph and its represented governed Artifacts and Structural Entities.

## Claim

a General Artifact Graph **means** the derived CAPRMEDIO Graph that represents governed Artifacts **and** Structural Entities as nodes, locates them by their authoritative Carriers, **and** connects them through the existing direct containment relations. its Structural Entity nodes include Scope Units **and** Atom Collections; its Artifact nodes include Atoms, Journals, **and** Projections.

node identities, Carrier locations, **and** containment come from existing authoritative sources **and** registered containment rules, **not** independently maintained graph declarations. an administrative directory does **not** become a Structural Entity merely because it is a folder. the graph provides their shared structural context **without** duplicating specialized graphs **or** becoming a separate source of authority.

## Details
