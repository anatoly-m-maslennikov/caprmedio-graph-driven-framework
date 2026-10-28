---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Parent
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Children
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Path
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Navigational Order Number
  - Subject/CAPRMEDIO/Carrier
version: 18
updated_at: 2026-10-27 19:59:56 +0400
relations: {}
atom_id: CA-R-1485
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Preserve consistent structural readability fields

## Scope

derived structural readability representations retained by a Project Structure.

## Claim

Project Structure **may** retain derived ancestry/path representations for readability **only** **when** their authoritative parent declarations **and** consistency constraints are explicit. a retained authority path **must** satisfy applicable Carrier naming **and** placement rules, including admitted exceptions; no retained Structural Level or other depth field is an authored Project Structure property. inconsistent representations **must** produce a reported conflict **without** an automatic choice of a new Name, parent, order, **or** binding. readability does **not** establish another source of authority.

## Details
