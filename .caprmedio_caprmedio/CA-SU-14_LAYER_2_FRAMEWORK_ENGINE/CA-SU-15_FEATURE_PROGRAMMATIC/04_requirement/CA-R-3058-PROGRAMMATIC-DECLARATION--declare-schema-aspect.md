---
identity:
  id: CA-R-3058
  ref_id: CA-R-3058
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Declaration
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Schema
  tier: 1
state:
  status: active
  version: 4
  updated_at: '2026-11-13T02:56:43.773790+00:00'
destination:
  file:
    name: CA-R-3058-PROGRAMMATIC-DECLARATION--declare-schema-aspect.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
author: Anatoly Maslennikov
---

## Summary

Declare Schema Aspect

## Claim

### Prose Claim

Schema is an Engineering Aspect within Data Handling.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Aspect
declare_entity(entity_name='Schema', instance=Aspect(address='PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Schema'))
```

## Semantics

The structure of derived records and their declared columns, formats and generation. A schema describes data structure; it is distinct from the data values and the files carrying them.
