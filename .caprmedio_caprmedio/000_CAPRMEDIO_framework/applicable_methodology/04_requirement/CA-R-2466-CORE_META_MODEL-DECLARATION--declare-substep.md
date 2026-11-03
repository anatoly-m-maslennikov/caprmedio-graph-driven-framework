---
atom_id: CA-R-2466
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)/Substep
version: 4
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2466-CORE_META_MODEL-DECLARATION--declare-substep.md
  source_atom_id: CA-R-2466
  source_atom_revision: 4
  source_sha256: 6f803901496d456e833a5fabe6d459d4ad0b787fe55578ba9ce3a2369d62ef49
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Substep

## Claim

```CFEL
Atom/(.Role: Operations)/Substep;
Substep//{:1}((IS_CONTAINED_BY)) Step//;
Substep//{:1}((RUNS)) Action//
```

## Semantics

A Substep is a leaf unit within a Step and runs exactly one reusable Action.
