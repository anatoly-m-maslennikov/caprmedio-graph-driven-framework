---
atom_id: CA-R-2232@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Package > Module > Code Unit
version: 1
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
tier: 1
---
## Summary

Define Code Unit

## Claim

A Code Unit is a code-level construct contained in exactly one Module, with Class and Function as specializations. It is distinct from an organizational Scope Unit.

### Formal claim

```text
Module > Code Unit
Code Unit/Class
Code Unit/Function
```

## Semantics

A Code Unit is a code-level construct, including Class and Function. It is distinct from the organizational Scope Unit. A Class and a Function retain their existing meanings; the classification does not merge them or turn them into project-scope containers.

## Details

A1250 records the name and subtypes; A1252 requires Module containment. Code Unit exists inside Module. A1253 records exactly-one whole per contained part. A1254 removes the Code wrapper: Modules belong to Packages. Tool is not silently mapped to Code Unit.
