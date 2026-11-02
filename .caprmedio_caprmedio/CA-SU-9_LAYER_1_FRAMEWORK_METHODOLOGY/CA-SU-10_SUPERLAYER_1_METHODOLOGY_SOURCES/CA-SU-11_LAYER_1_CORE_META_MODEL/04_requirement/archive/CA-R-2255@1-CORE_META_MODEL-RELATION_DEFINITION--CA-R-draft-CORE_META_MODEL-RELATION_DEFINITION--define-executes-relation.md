---
atom_id: CA-R-2255@1
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
version: 1
relations: {}
tier: 1
updated_at: 2026-10-29 07:51:41 +0400
---
## Summary

Define EXECUTES Relation

## Claim

EXECUTES connects an actual Runtime to a Workflow Run it executes. The stored direction is Runtime to Workflow Run. IS_EXECUTED_BY is its declared derived inverse and is not a second stored fact.

### Formal claim

```yaml
relation_type: EXECUTES
meaning: Connect an actual Runtime to the Workflow Run it executes.
derived_inverse: IS_EXECUTED_BY
stored_fact: direct_only
```

## Details

This named Type uses the general `((RELATION_TYPE))` form. It has no dedicated short Subject operator. This Draft defines neither an existing Runtime nor a Workflow Run relation fact.
