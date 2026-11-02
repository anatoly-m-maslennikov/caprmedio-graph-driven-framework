---
subjects:
  governs: "Entity/Continuant/Relation/Type: CONTAINS"
  depends_on:
  - "Entity/Continuant/Node/Atom.Enabled Relations.Contains"
  - "Entity/Continuant/Node/Scope Unit"
version: 12
updated_at: "2026-10-18 03:33:24 +0400"
relations: {}
atom_id: "CA-R-1368"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Containment Relation Pair

## Scope

Direct containment and its derived inverse, including Scope Unit containment and enabled Atom containment.

## Claim

the Containment Relation Pair **means** direct relation `CONTAINS` **and** its inverse-derived relation `IS_CONTAINED_BY`. a Scope Unit **may** contain other Scope Units **and** governed content. an Atom **may** contain other Atoms **when** containment is enabled for its Content Role **or** Type.

## Details

`IS_CONTAINED_BY` is derived from `CONTAINS`; it is not independently authored. Containment does not make a contained Atom part of the containing Atom's Substance or change its owning Scope Unit. This relation definition does not implement or require a construction graph projection.

