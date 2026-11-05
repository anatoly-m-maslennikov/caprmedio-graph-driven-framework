---
atom_id: CA-R-2530
ref_id: CA-R-2530
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.Path
version: 2
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Declaration
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2530-CORE_META_MODEL-DECLARATION--declare-scope-unit-path.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Scope Unit Path

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.Path{::1}:: [string]{::1+};

Scope Unit.Path.*[]{::0}
```

### Prose Claim


The Path lists Scope Unit identities along the complete declared containment chain from the root to the addressed Scope Unit.

