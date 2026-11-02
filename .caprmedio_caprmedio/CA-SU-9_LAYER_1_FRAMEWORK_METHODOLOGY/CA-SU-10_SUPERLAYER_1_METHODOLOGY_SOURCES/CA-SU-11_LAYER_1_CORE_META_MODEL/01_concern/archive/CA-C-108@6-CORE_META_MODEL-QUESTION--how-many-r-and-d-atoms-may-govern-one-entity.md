---
atom_id: CA-C-108@6
priority: low
subjects:
  governs: Entity
  depends_on:
  - Entity/Continuant/Object/Atom
  - Atom/Claim
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Entity/Continuant/Object/Scope Unit
  - Atom/Tier/Local Tier
version: 6
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
content_role: "Concern"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: Archived
author: "Anatoly Maslennikov"
type: "Question"
global_tier: 11
---
# How many R and D Atoms may govern one Entity?

what limits, **if** **any**, should apply **to** the number of Requirement **and** Delivery Atoms that govern the same Entity while expressing distinct Claims?

## Context

the Operator can envisage cases requiring **`>1`** Requirement Atom for the same Entity because the Claims differ. the earlier proposed limit of **`<=1`** Requirement Atom **and** **`<=1`** Delivery Atom per Entity remains unresolved. distinct Claims **and** duplicated authority for the same Claim are different cases; correctly assigned Subjects, applicable Scope Units, **and** Local Tiers require consideration **before** choosing a rule.

## Disposition

deferred for later consideration at the Operator's request. this Concern records an open design question; it does **not** establish a cardinality rule **or** block the current migration.
