---
atom_id: CA-R-2466
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Substep
version: 4
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2466-CORE_META_MODEL-DECLARATION--declare-substep.md
  source_atom_id: CA-R-2466
  source_atom_revision: 4
  source_sha256: f2a40705628b526539a0422901b2e5032ffaec8f0900072fb9c4d8d89b20bd11
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Substep

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Operations)/Substep;

# instances
Substep//$substep{:1}((IS_CONTAINED_BY)) Step//$step;

Substep//$substep_2{:1}((RUNS)) Action//$action
```

## Semantics

A Substep is a leaf unit within a Step and runs exactly one reusable Action.
