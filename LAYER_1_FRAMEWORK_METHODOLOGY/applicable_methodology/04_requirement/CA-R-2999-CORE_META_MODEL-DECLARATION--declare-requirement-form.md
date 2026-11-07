---
atom_id: CA-R-2999
ref_id: CA-R-2999
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Requirement)
tier: 3
status: Active
version: 2
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-2999-CORE_META_MODEL-DECLARATION--declare-requirement-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2999-CORE_META_MODEL-DECLARATION--declare-requirement-form.md
  source_atom_id: CA-R-2999
  source_atom_revision: 2
  source_sha256: 60c1a0e7e7a4d261afe61dfee699e91ddb9efe076a0ccfc71623404859d3fd93
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Requirement Form

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Form := Requirement);

# instances
Atom/(.Header.Form := Requirement)//$requirement.Header.Role:: [in (Requirement)]{::1}
```

## Semantics

A Requirement Form states a local required outcome, behavior, property or constraint.
