---
atom_id: CA-R-2540
ref_id: CA-R-2540
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection.Source.Atoms
version: 2
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Declaration
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2540-CORE_META_MODEL-DECLARATION--declare-projection-source-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Projection.Source.Atoms

## Claim

### Formal Claim

```CFEL
# model
Projection.Source.Atoms{::0..1}:: [string]{::0+};

Projection.Source.Atoms.*[]{::0}
```

### Prose Claim



Each value is an Atom ID with an explicit Version.
