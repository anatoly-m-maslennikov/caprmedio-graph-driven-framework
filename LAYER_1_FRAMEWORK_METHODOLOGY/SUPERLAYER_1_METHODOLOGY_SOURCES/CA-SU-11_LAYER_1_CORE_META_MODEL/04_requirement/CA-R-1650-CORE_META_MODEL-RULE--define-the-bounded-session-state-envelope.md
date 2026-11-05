---
atom_id: CA-R-1650
ref_id: CA-R-1650
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Data Validation
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Runtime/Session
tier: 2
status: Active
version: 34
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1650-CORE_META_MODEL-RULE--define-the-bounded-session-state-envelope.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define the bounded session-state envelope

## Claim

### Prose Claim


the bounded session-state envelope.


the bounded session-state envelope **must** contain **only** routing invariants, current scope, applicable settings, compact session state, **and** references needed **to** load active authority on demand.
