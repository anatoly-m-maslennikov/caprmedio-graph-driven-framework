---
atom_id: CA-R-2467
ref_id: CA-R-2467
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2467-CORE_META_MODEL-DECLARATION--declare-action.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2467-CORE_META_MODEL-DECLARATION--declare-action.md
  source_atom_id: CA-R-2467
  source_atom_revision: 2
  source_sha256: a3273b8062e8fea35866131908d3b0495296e55779e43d20f5046067414fb068
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Action

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Operations)/Action;

# instances
Action//$action{::0+}((IS_RUN_BY)) (in (Step, Substep))//$selected
```

## Semantics

An Action is a reusable operational building block. Its boundary reflects one modeled responsibility.
