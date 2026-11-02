---
atom_id: CA-R-2255@5
content_role: Requirement
type: Relation Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Relation//EXECUTES
  depends_on:
  - Entity/Object/Occurrent/Runtime
  - Entity/Object/Occurrent/Execution/Workflow Run
version: 5
relations: {}
tier: 1
updated_at: 2026-10-29 10:21:17 +0400
---
## Summary

Define EXECUTES Relation

## Claim

EXECUTES connects an actual Runtime to a Workflow Run it executes. The stored direction is Runtime to Workflow Run. IS_EXECUTED_BY is its declared derived inverse and is not a second stored fact.

### Formal claim

```text
Entity/Graph Syntax > Relation//EXECUTES
Entity/Graph Syntax > Relation//IS_EXECUTED_BY
```

## Details

This named Type uses the general `((RELATION_TYPE))` form. It has no dedicated short Subject operator. This defines the reusable Type and its derived reverse view; it creates no Runtime or actual endpoint tuple.
