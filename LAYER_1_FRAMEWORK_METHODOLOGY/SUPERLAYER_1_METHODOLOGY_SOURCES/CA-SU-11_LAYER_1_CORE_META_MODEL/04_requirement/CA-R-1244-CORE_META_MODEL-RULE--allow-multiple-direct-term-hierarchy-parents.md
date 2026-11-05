---
atom_id: CA-R-1244
ref_id: CA-R-1244
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER_THAN
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/(.Form: Terms Graph)'
  - CAPRMEDIO_MODEL <+ Term
tier: 2
status: Active
version: 33
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1244-CORE_META_MODEL-RULE--allow-multiple-direct-term-hierarchy-parents.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Allow multiple direct Term hierarchy parents

## Claim

### Prose Claim


Direct NARROWER_THAN parents of a Term.


a Term **may** have **`>=0`** direct NARROWER_THAN parents.
