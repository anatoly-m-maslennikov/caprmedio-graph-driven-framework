---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project.Structure
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Parent
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Children
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Path
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Navigational Order Number
  - Subject/Graph Node/Carrier
version: 17
updated_at: 2026-10-27 06:04:45 +0400
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
