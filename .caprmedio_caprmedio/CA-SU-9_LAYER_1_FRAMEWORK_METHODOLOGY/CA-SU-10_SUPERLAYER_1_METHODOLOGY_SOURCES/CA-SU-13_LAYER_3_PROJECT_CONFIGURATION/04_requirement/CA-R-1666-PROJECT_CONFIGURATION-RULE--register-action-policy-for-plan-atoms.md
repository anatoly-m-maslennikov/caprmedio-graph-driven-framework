---
atom_id: CA-R-1666
ref_id: CA-R-1666
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Form'
tier: 2
relations:
  depends_on:
  - CA-R-1286
status: Active
version: 37
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1666-PROJECT_CONFIGURATION-RULE--register-action-policy-for-plan-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Register Action Policy for Plan Atoms

## Claim

### Prose Claim


the CAPRMEDIO Project Configuration registration of `Atom/(.Header.Role := Plan).Header.Form` values.


the CAPRMEDIO Project Configuration **must** register Action Policy as an additional value of `Atom/(.Header.Role := Plan).Header.Form`; Plan retains its canonical admission under CA-R-1574@21-CORE_META_MODEL-DEFINITION--define-the-common-plan-atom; navigation Labels do **not** add further Type values.
