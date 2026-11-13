---
atom_id: CA-R-2965
ref_id: CA-R-2965
container:
  scope_unit: CA-SU-11
role: Requirement
form: Relation Declaration
topics:
  main_subject: CAPRMEDIO_MODEL/CFEL/Relation//IS_ORDERED_RIGHT_AFTER
tier: 3
status: active
version: 2
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-2965-CORE_META_MODEL-RELATION_DECLARATION--declare-is-ordered-right-after.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare IS_ORDERED_RIGHT_AFTER

## Claim

### Prose Claim

The Host and Target are declared model Properties of the same immediate bearer, selected from the applicable Atom.Header or Atom.Content Property structure. The Host follows the Target immediately in the declared sibling order. Ordering is acyclic; each Property has at most one immediate predecessor and at most one immediate successor. The inverse alias IS_ORDERED_RIGHT_BEFORE reverses that reading; it denotes the same ordering fact.

`x ;> y` means x is immediately before y, in the order x; y. `x <; y` means x is immediately after y, in the order y; x. These Relations specify model Property order; they do not create runtime Property instances or copy facts.

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_relation

declare_relation(
    relation_name='IS_ORDERED_RIGHT_AFTER',
    source_endpoint={'level': 'model_entities', 'entity_paths': ('Atom.Header.**', 'Atom.Content.**')},
    target_endpoint={'level': 'model_entities', 'entity_paths': ('Atom.Header.**', 'Atom.Content.**')},
    inverse_alias='IS_ORDERED_RIGHT_BEFORE',
    written_alias='<;',
    reverse_written_alias=';>',
    targets_per_source=Cardinality(minimum=0, maximum=1),
    sources_per_target=Cardinality(minimum=0, maximum=1),
    same_immediate_bearer=True,
    acyclic=True,
)
```

## Semantics

IS_ORDERED_RIGHT_AFTER relates a model Property to its immediately preceding sibling Property.
