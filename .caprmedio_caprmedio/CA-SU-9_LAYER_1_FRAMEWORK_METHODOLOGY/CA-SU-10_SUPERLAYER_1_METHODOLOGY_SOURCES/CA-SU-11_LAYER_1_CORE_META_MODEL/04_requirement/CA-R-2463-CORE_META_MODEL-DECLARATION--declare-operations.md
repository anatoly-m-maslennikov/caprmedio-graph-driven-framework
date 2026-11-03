---
atom_id: CA-R-2463
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Operations

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role: Operations)
```

## Semantics

An Operations Atom defines reusable work. It can define an Action, a Workflow, a Step, or a Substep.
