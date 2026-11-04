---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")/(.Header.Form := Analysis Report)
version: 26
updated_at: 2026-11-02 19:33:47 +0400
relations:
  child_of:
  - CA-R-1702
atom_id: CA-R-1556
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1556-CORE_META_MODEL-RULE--keep-analysis-optional-before-specification.md
  source_atom_id: CA-R-1556
  source_atom_revision: 26
  source_sha256: 9839bc8523b7fc1abc88ce2503fd4dcd4f116f0eee492f99b60b103abf0bd15f
  original_relations_sha256: 86f48d79fbbfe66ffab2b0bb686a446bbbe206535c96d6e0d3b25f21670f9677
---
## Summary

Keep Analysis optional before specification

## Claim

### Prose Claim


AI Agent creation of Spec Atoms and optional Analysis Reports before specification.


an identified AI Agent **may** create Spec Atoms directly from sufficiently clear Operator input **when** active Operator authority permits the required actions.

an Analysis Report **may** precede **and** inform Spec **when** investigation **or** synthesis is useful. it is **not** a mandatory Carrier **or** gate for **every** Spec Claim.

