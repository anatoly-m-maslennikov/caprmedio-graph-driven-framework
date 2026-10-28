---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Expansion Boundary
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//CORE_META_MODEL
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Extension Sources
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
version: 29
updated_at: 2026-10-27 19:59:54 +0400
relations: {}
atom_id: CA-R-1375
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Restrict Methodology Source Expansion to Core Permission

## Scope

Methodology source expansion by an Extension **or** Project Configuration.

## Claim

an Extension **or** Project Configuration **must** add Claims, Terms, allowed values, Types, Methods, Evaluations, Deliveries, Operations, activation rules, compatibility rules, **or** priority rules **only** **where** one active CORE_META_MODEL Atom permits the addition **and** **must not** redefine, replace, shadow, weaken, delete, contradict, reinterpret, **or** mutate Core Meta-Model authority at **any** numeric Tier; an Atom's numeric Tier alone grants no exception **to** this source authority boundary.

## Details

current Extension activation **and** selected Extension Revisions remain owned by Framework Instance Settings under CA-R-1207. permission **to** add a rule does **not** duplicate **or** transfer ownership of its current selection.
