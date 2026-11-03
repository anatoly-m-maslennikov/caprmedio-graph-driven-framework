---
atom_id: CA-R-2464
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow
version: 4
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Workflow

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Operations)/Workflow;

# instances
Workflow//$workflow{:1+}((CONTAINS)) Step//$step;

Workflow//$workflow_2{:0+}((IS_RUN_BY)) Step//$step_2
```

## Semantics

A Workflow defines a graph of Steps for governed work.
