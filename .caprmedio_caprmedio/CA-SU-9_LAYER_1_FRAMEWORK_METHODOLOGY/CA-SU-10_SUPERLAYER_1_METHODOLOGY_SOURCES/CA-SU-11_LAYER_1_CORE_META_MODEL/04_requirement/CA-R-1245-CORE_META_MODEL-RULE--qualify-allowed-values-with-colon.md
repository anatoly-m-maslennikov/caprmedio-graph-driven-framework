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
version: 29
updated_at: '2026-11-11 14:06:22 +0400'
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

A declaration with an allowed-value Main Subject `X := Y` states `X :: Y;` in its Formal Claim. For the qualified Subject `B/(.p := V)`, write `B.p :: V;`. Preserve parent qualifiers as conditions on B. The Formal Claim supplies its complete scope. Put instance constraints in a separate `FOR EACH ... : (...)` expression.
