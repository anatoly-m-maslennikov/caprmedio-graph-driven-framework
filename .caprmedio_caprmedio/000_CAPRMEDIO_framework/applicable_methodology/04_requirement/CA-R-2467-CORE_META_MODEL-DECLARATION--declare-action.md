---
atom_id: CA-R-2467
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)/Action
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2467-CORE_META_MODEL-DECLARATION--declare-action.md
  source_atom_id: CA-R-2467
  source_atom_revision: 2
  source_sha256: 67d18f321c2a4b8bdefcf95518a333a6e621b35421a1ce08b3d6b5f02267b82f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Action

## Claim

```CFEL
Atom/(.Role: Operations)/Action;
Action//{:0+}((IS_RUN_BY)) (in (Step, Substep))//
```

## Semantics

An Action is a reusable operational building block. Its boundary reflects one modeled responsibility.
