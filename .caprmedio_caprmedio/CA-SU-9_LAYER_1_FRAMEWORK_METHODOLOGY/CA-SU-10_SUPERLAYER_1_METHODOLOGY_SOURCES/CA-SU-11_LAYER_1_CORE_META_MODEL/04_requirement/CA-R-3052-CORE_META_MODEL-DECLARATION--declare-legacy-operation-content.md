---
identity:
  id: CA-R-3052
  ref_id: CA-R-3052
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations).Content.Operation
  tier: 4
state:
  status: active
  version: 3
  updated_at: '2026-11-12T18:59:51.161573+00:00'
destination:
  file:
    name: CA-R-3052-CORE_META_MODEL-DECLARATION--declare-legacy-operation-content.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
author: Anatoly Maslennikov
---

## Summary

Declare legacy Operation content

## Claim

### Prose Claim

An Operations Atom may retain its legacy Operation section during migration. Operation is a Markdown Content Property. Its presentation subheadings, lists and code blocks remain part of its value.

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name='Operation',
    relation_name='IS_PROPERTY_OF',
    base_path='Atom.Content',
    applies_to_entity_classes=['Operations'],
    value_format='markdown',
    value_cardinality=Cardinality(minimum=0, maximum=1),
    dependent_property_cardinality=0,
)
```

## Semantics

Operation is the operation text carried by the legacy Operations Atom. This declaration describes that existing section; it does not decide whether a later Form must use Operation or Claim.
