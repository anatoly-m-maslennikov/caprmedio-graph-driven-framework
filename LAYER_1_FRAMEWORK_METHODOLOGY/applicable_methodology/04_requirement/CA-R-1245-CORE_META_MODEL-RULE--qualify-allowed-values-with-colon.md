---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity
  passive:
  - CAPRMEDIO_MODEL <+ CFEL<+Operator//AllowedValue
  - CAPRMEDIO_MODEL <+ Term//Property
version: 28
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1245
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1245-CORE_META_MODEL-RULE--qualify-allowed-values-with-colon.md
  source_atom_id: CA-R-1245
  source_atom_revision: 28
  source_sha256: 0dbf7796de969c987d6fa8380af15191629f19b005875b4cfdc88975ffcee674
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Qualify Allowed Values with Colon

## Claim

### Prose Claim


allowed-value qualification in a Subject Expression.


**in** a Subject Expression, `X:Y` **must** admit Y as one possible value of X in X's qualified context, irrespective of X's kind or path. This qualification is a CFEL operator, not a graph Relation. It does not assign Y to an occurrence or determine direct-value cardinality.
