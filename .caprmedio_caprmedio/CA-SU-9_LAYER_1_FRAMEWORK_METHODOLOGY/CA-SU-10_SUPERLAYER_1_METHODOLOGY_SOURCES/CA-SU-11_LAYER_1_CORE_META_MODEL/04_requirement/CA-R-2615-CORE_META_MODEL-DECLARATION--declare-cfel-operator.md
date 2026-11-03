---
atom_id: CA-R-2615
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL<+Operator//SubjectValueSelection
version: 1
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare CFEL operator :=

## Claim

### Formal Claim

```CFEL
# model
Operator//SubjectValueSelection == ":="
```

## Semantics

In a Subject, combine an admitted Property value with selection; it is not assignment.
