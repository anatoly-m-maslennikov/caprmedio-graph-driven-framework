---
atom_id: CA-R-3004
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Approach Policy)
tier: 3
ref_id: CA-R-3004
status: Active
version: 2
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-3004-CORE_META_MODEL-DECLARATION--declare-approach-policy-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-3004-CORE_META_MODEL-DECLARATION--declare-approach-policy-form.md
  source_atom_id: CA-R-3004
  source_atom_revision: 2
  source_sha256: e16a38aa2bd46b8c30d34afe49351452c074a6850e2c3b18c4f0f60533a39553
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Approach Policy Form

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Form := Approach Policy);

# instances
Atom/(.Header.Form := Approach Policy)//$approach_policy.Header.Role:: [in (Requirement, Method, Evaluation, Delivery, Operations)]{::1}
```

## Semantics

An Approach Policy is conditional on its stated case. At every descendant where that case applies, a local Atom must bind the Policy to the actual case through SPECIALIZES. A reference alone is insufficient; the binding preserves parent constraints.
