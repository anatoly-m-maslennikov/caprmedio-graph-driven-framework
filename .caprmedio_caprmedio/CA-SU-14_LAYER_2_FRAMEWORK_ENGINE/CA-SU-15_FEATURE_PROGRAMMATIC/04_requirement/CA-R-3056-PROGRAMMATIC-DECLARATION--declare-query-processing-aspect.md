---
identity:
  id: CA-R-3056
  ref_id: CA-R-3056
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Declaration
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Query Processing
  tier: 1
state:
  status: active
  version: 4
  updated_at: '2026-11-13T02:56:07.651537+00:00'
destination:
  file:
    name: CA-R-3056-PROGRAMMATIC-DECLARATION--declare-query-processing-aspect.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
author: Anatoly Maslennikov
---

## Summary

Declare Query Processing Aspect

## Claim

### Prose Claim

Query Processing is an Engineering Aspect within Data Handling.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Aspect
declare_entity(entity_name='Query Processing', instance=Aspect(address='PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Query Processing'))
```

## Semantics

Execution of accepted queries and transformations of their materialized results, including paging, filtering, ordering and grouping. Query authoring governs how query text is written; Source Retrieval governs how input files are read.
