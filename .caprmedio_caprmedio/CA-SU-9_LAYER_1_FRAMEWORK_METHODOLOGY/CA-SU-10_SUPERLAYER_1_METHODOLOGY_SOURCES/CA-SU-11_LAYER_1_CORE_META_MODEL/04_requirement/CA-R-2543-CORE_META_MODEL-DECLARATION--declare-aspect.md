---
atom_id: CA-R-2543
ref_id: CA-R-2543
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Aspect
tier: 3
status: active
version: 5
updated_at: '2026-11-12T17:40:07+00:00'
carrier_destination:
  file:
    name: CA-R-2543-CORE_META_MODEL-DECLARATION--declare-aspect.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Aspect

## Claim

### Prose Claim



- MODEL declares the generic Aspect.
- All concrete Aspects are instances in the applicable PROJECT STRUCTURE tree.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Node

class Aspect(Node):
    pass

declare_entity(entity_class=Aspect, entity_name='Aspect')
```

## Semantics

An Aspect is a topic through which an Atom addresses its Subject.
