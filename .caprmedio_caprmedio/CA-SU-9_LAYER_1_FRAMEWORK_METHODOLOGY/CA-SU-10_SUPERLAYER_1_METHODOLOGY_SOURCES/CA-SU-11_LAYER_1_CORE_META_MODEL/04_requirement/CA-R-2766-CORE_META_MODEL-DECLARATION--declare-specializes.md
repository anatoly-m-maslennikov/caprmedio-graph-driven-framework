---
atom_id: CA-R-2766
ref_id: CA-R-2766
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//SPECIALIZES
tier: 1
status: active
version: 3
updated_at: 2026-11-05 18:23:39 +0400
carrier_destination:
  file:
    name: CA-R-2766-CORE_META_MODEL-DECLARATION--declare-specializes.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare SPECIALIZES

## Claim

### Prose Claim

The child Atom's Claim is more specific or stricter than the parent Atom's Claim in the same or a narrower Scope and preserves the parent's applicable constraints. A conditional specialization is included. A reference or dependency alone does not establish SPECIALIZES. IS_SPECIALIZED_BY is the inverse alias, with parent and child endpoints reversed.

### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name="SPECIALIZES",
    source_endpoint={"level": "instances", "entity_paths": ("Atom",)},
    target_endpoint={"level": "instances", "entity_paths": ("Atom",)},
    inverse_alias="IS_SPECIALIZED_BY",
)
```

## Semantics

SPECIALIZES relates a child Atom to the Atom whose Claim it specializes.
