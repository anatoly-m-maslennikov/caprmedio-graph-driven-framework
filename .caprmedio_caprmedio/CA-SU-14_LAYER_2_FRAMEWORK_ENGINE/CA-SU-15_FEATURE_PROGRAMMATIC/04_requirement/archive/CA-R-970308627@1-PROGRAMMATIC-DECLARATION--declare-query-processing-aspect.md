---
identity:
  id: CA-R-970308627
  ref_id: CA-R-970308627@1
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Declaration
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data
      Handling <+ Query Processing
  tier: 1
state:
  status: Archived
  version: 1
  updated_at: 2026-11-09 07:45:15 +0400
destination:
  file:
    name: CA-R-970308627@1-PROGRAMMATIC-DECLARATION--declare-query-processing-aspect.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archive
author: Anatoly Maslennikov
---

## Summary

Declare Query Processing Aspect

## Claim

### Prose Claim

Query Processing is an Engineering Aspect within Data Handling.

### Formal Claim

```CFEL
# model
CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Query Processing;
```

## Semantics

Execution of accepted queries and transformations of their materialized results, including paging, filtering, ordering and grouping. Query authoring governs how query text is written; Source Retrieval governs how input files are read.
