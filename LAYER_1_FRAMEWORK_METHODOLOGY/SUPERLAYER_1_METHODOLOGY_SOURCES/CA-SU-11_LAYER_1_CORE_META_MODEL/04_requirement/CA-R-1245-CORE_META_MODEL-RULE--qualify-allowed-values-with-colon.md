---
atom_id: CA-R-1245
ref_id: CA-R-1245
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL<+Operator//AllowedValue
  - CAPRMEDIO_MODEL <+ Term//Property
tier: 3
status: Active
version: 28
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-1245-CORE_META_MODEL-RULE--qualify-allowed-values-with-colon.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Qualify Allowed Values with Colon

## Claim

### Prose Claim


allowed-value qualification in a Subject Expression.


**in** a Subject Expression, `X:Y` **must** admit Y as one possible value of X in X's qualified context, irrespective of X's kind or path. This qualification is a CFEL operator, not a graph Relation. It does not assign Y to an occurrence or determine direct-value cardinality.
