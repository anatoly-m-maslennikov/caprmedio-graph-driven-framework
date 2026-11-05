---
atom_id: CA-R-1665
ref_id: CA-R-1665
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery).Header.Form'
tier: 3
status: Active
version: 35
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1665-PROJECT_CONFIGURATION-RULE--register-type-values-for-delivery-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1665-PROJECT_CONFIGURATION-RULE--register-type-values-for-delivery-atoms.md
  source_atom_id: CA-R-1665
  source_atom_revision: 35
  source_sha256: 16d6b236f9e0e45680b435bd9874a7be749462b633b5b21159b7854b2168b81e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Type Values for Delivery Atoms

## Claim

### Prose Claim


`Atom/(.Header.Role := Delivery).Header.Form` values.


Policy and Decision are the Delivery Type values for reusable delivery rules and bounded delivery choices. Release and Environment describe governed things or applicability; they do not require separate Delivery Types.

## Details

Policy and Decision are defined by CA-R-2267@2 and CA-R-2268@1. Delivery Atoms use these meanings independently of their Subjects. Registration does not constrain a Type value to a particular Tier.
