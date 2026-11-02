---
atom_id: CA-R-2177@5
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Object/Continuant/Package > Module
version: 5
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
tier: 3
---
## Summary

Define Module

## Claim

A Module is a file-level Implementation component executable by its corresponding language engine, compiled or interpreted as applicable. A Module can implement runtime functionality or evaluations, including tests. Each Module is carried by exactly one File.

### Formal claim

```text
Package > Module
Module > Code Unit
Module ((IS_CARRIED_BY)) File
```

## Semantics

Module identifies the logical component; File is its Carrier. A Module belongs to one Package, including the root Package for an otherwise standalone file. A Code Unit is a construct inside its Module. Logical containment is distinct from filesystem representation.
