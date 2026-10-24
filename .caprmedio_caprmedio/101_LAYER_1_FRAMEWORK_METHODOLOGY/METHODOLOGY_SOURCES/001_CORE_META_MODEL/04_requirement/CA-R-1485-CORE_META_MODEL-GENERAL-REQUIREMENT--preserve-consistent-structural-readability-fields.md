---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Structure
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Scope Unit.Parent
  - Subject/Domain/Node/Continuant/Scope Unit.Children
  - Subject/Domain/Node/Continuant/Scope Unit.Path
  - Subject/Domain/Node/Continuant/Scope Unit.Navigational Order Number
  - Subject/Engineering/Carrier
version: 13
updated_at: 2026-10-24 01:37:42 +0400
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
