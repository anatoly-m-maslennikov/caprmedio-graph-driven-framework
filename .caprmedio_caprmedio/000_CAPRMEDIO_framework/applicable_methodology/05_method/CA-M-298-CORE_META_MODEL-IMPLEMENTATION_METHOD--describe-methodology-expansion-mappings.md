---
atom_id: CA-M-298
ref_id: CA-M-298
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_META_MODEL
tier: 2
relations:
  child_of:
  - CA-M-006
  method_for:
  - CA-R-1375
status: Active
version: 26
updated_at: 2026-11-02 18:35:20 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-298-CORE_META_MODEL-IMPLEMENTATION_METHOD--describe-methodology-expansion-mappings.md
  source_atom_id: CA-M-298
  source_atom_revision: 26
  source_sha256: 0e63f24408baa99ff384b366b9658dd27a98e899980f9817963b4f7cc808cb8b
  original_relations_sha256: 7e5e58e1c9bed41c0ded2593d8cbcc64b300c073a390fbc4f30a646c8fc641fa
---
## Summary

Describe methodology expansion mappings

## Claim

### Prose Claim


Methodology Source expansion mappings.


**to** describe a Methodology Source expansion mapping, use **`=1`** explicit mapping description that identifies:

- the source element **and** its provenance;
- the exact canonical target;
- the mapping rule;
- the intended scope of application;
- the applicable Core Meta-Model distinctions at **any** Local Tier.

apply this same mapping convention **to** Extension **and** Project Configuration sources regardless of provenance. the convention supports CA-R-1375-CORE_META_MODEL-CORE-REQUIREMENT--restrict-methodology-source-expansion-to-core-permission's expansion boundary; it does **not** admit activation **or** reliance. CA-O-054-CORE_META_MODEL-ACTION--admit-methodology-expansion-mappings owns that admission Action **and** re-evaluation following material changes.
