---
atom_id: CA-R-1248@22
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity
version: 22
relations: {}
tier: 1
updated_at: 2026-10-29 07:32:39 +0400
---
## Summary

Define Entity

## Claim

Entity is the common category for every primary graph node and every dependent property in the framework. Object is one specialization, alongside Aspect, Graph Syntax and Carrier. Not every Entity is an Object. These categories separate abstract Objects, topics, syntax and storage representation; no occurrence is identified with its persistent record.

### Formal claim

```text
Entity/Object
Object/Continuant
Object/Occurrent
Entity/Aspect
Entity/Graph Syntax
Entity/Carrier
Graph Syntax > Relation
Graph Syntax > Format
Graph Syntax > Cardinality
```

## Details

A1302 records the latest root decision. This replaces the old Model-root preparation for adoption; no Current source or runtime is changed.
