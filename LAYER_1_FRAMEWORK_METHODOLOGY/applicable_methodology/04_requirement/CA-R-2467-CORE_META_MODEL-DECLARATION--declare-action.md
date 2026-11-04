---
atom_id: CA-R-2467
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2467-CORE_META_MODEL-DECLARATION--declare-action.md
  source_atom_id: CA-R-2467
  source_atom_revision: 2
  source_sha256: 8b86d2c1204c2a881b01ee7381be3dd7eff9e89a2975e00ccae45444b20ba11a
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
Action//$action{:0+}((IS_RUN_BY)) (in (Step, Substep))//$selected
```

## Semantics

An Action is a reusable operational building block. Its boundary reflects one modeled responsibility.
