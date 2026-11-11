---
atom_id: CA-M-298
ref_id: CA-M-298
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Authoring"
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
