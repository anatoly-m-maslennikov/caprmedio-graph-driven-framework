---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - Entity/Graph Syntax > Relation
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Label'
version: 24
updated_at: 2026-10-29 17:09:47 +0400
relations: {}
atom_id: CA-R-1578@24
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Define Hub Atom as a derived description

## Claim scope

Hub Atom descriptions.

## Claim

Hub Atom **means** a derived description of a Plan Atom with **`>0`** outgoing derived `CONTAINS` links to Plan Atoms; it does **not** introduce another Type, Subtype, stored classification, identity, **or** authority tier. contained Atoms retain their own Claims rather than becoming parts of the Hub Claim.
