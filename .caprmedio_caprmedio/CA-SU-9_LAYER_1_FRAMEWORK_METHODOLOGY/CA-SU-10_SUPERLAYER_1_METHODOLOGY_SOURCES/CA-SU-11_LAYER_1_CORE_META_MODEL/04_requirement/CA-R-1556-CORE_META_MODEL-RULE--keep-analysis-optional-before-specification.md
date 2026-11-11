---
atom_id: CA-R-1556
ref_id: CA-R-1556
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := "Analysis and Advisory")/(.Header.Context.Form := Analysis Report)
tier: 2
relations:
  child_of:
  - CA-R-1702
status: Active
version: 26
updated_at: 2026-11-02 19:33:47 +0400
carrier_destination:
  file:
    name: CA-R-1556-CORE_META_MODEL-RULE--keep-analysis-optional-before-specification.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Keep Analysis optional before specification

## Claim

### Prose Claim


AI Agent creation of Spec Atoms and optional Analysis Reports before specification.


an identified AI Agent **may** create Spec Atoms directly from sufficiently clear Operator input **when** active Operator authority permits the required actions.

an Analysis Report **may** precede **and** inform Spec **when** investigation **or** synthesis is useful. it is **not** a mandatory Carrier **or** gate for **every** Spec Claim.

