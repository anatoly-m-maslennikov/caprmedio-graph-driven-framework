---
atom_id: CA-R-2687
role: Requirement
form: Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit.order
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit
relations: {}
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2687-CORE_META_MODEL-DECLARATION--declare-scope-unit-order.md
  source_atom_id: CA-R-2687
  source_atom_revision: 1
  source_sha256: 425b43b853867bda555b74525c164f602466704c3c9b8ebfc2416246a2ad2eec
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Scope Unit.order

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.order: []{:0};

Scope Unit.order.*[in (ordered, number)]{:1..2}
```

## Semantics

order groups the Boolean ordered and the conditional number as sibling Properties. The group has no direct value.
