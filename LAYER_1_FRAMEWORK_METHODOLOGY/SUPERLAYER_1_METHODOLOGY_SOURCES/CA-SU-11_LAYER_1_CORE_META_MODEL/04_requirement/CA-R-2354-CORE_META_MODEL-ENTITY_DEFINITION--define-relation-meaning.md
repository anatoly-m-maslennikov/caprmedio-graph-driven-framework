---
atom_id: CA-R-2354
ref_id: CA-R-2354
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation.Meaning
tier: 1
status: Active
version: 7
updated_at: 2026-11-04 22:00:28 +0400
carrier_destination:
  file:
    name: CA-R-2354-DECLARATION--define-relation-meaning.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define Relation Meaning

## Claim

### Prose Claim


Relation Meaning is the canonical meaning of a reusable Relation Type.
### Formal Claim

```CFEL
# model
Relation.Meaning{::1}:: [string]{::1};

Relation.Meaning.*[]{::0}
```

