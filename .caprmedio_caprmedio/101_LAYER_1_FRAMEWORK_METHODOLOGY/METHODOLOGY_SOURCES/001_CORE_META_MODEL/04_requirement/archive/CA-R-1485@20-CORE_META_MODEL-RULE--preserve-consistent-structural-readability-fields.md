---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Children
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Path
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Navigational Order Number
  - Entity/Carrier
version: 20
updated_at: 2026-10-29 07:45:27 +0400
relations: {}
atom_id: CA-R-1485@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Preserve consistent structural readability fields

## Claim scope

derived structural readability representations retained by a Project Structure.

## Claim

Project Structure **may** retain derived ancestry/path representations for readability **only** **when** their authoritative parent declarations **and** consistency constraints are explicit. a retained authority path **must** satisfy applicable Carrier naming **and** placement rules, including admitted exceptions; no retained Structural Level or other depth field is an authored Project Structure property. inconsistent representations **must** produce a reported conflict **without** an automatic choice of a new Name, parent, order, **or** binding. readability does **not** establish another source of authority.

## Details
