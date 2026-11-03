---
subjects:
  active: CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Authoring
  passive:
  - CAPRMEDIO <+ MODEL <+ Scope Unit
  - CAPRMEDIO <+ STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  - CAPRMEDIO <+ STRUCTURE <+ Scope Unit//CORE_META_MODEL
version: 26
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-006
  method_for:
  - CA-R-1375
atom_id: CA-M-298
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 2
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-298-CORE_META_MODEL-IMPLEMENTATION_METHOD--describe-methodology-expansion-mappings.md
  source_atom_id: CA-M-298
  source_atom_revision: 26
  source_sha256: d1b02a826e0e9394763463a4a18fd2caa06a67365a77bbd21dc60af0ec5546c5
  original_relations_sha256: 7e5e58e1c9bed41c0ded2593d8cbcc64b300c073a390fbc4f30a646c8fc641fa
---
## Summary

Describe methodology expansion mappings

## Claim scope

Methodology Source expansion mappings.

## Claim

**to** describe a Methodology Source expansion mapping, use **`=1`** explicit mapping description that identifies:

- the source element **and** its provenance;
- the exact canonical target;
- the mapping rule;
- the intended scope of application;
- the applicable Core Meta-Model distinctions at **any** Local Tier.

apply this same mapping convention **to** Extension **and** Project Configuration sources regardless of provenance. the convention supports CA-R-1375-CORE_META_MODEL-CORE-REQUIREMENT--restrict-methodology-source-expansion-to-core-permission's expansion boundary; it does **not** admit activation **or** reliance. CA-O-054-CORE_META_MODEL-ACTION--admit-methodology-expansion-mappings owns that admission Action **and** re-evaluation following material changes.
