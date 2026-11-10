---
atom_id: CA-C-108
ref_id: CA-C-108@7
container:
  scope_unit: CA-SU-11
role: Concern
form: Question
topics:
  main_subject: Entity
  dependencies:
  - Entity/Continuant/Object/Atom
  - Atom/Claim
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Subject/Domain/Node/Continuant/Scope Unit
  - Atom/Tier/Local Tier
status: Archived
version: 7
updated_at: 2026-10-23 03:14:50 +0400
priority: low
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
global_tier: 11
carrier_destination:
  file:
    name: CA-C-108@7-CORE_META_MODEL-QUESTION--how-many-r-and-d-atoms-may-govern-one-entity.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/01_concern/archive
---
# How many R and D Atoms may govern one Entity?

what limits, **if** **any**, should apply **to** the number of Requirement **and** Delivery Atoms that govern the same Entity while expressing distinct Claims?

## Context

the Operator can envisage cases requiring **`>1`** Requirement Atom for the same Entity because the Claims differ. the earlier proposed limit of **`<=1`** Requirement Atom **and** **`<=1`** Delivery Atom per Entity remains unresolved. distinct Claims **and** duplicated authority for the same Claim are different cases; correctly assigned Subjects, applicable Scope Units, **and** Local Tiers require consideration **before** choosing a rule.

## Disposition

deferred for later consideration at the Operator's request. this Concern records an open design question; it does **not** establish a cardinality rule **or** block the current migration.
