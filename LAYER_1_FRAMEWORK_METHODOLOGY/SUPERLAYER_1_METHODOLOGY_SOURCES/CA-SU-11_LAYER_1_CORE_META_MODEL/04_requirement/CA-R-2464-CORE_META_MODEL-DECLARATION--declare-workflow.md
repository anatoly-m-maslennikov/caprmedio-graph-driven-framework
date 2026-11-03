---
atom_id: CA-R-2464
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)/Workflow
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

```CFEL
Atom/(.Role: Operations)/Workflow;
Workflow//{:1+}((CONTAINS)) Step//;
Workflow//{:0+}((IS_RUN_BY)) Step//
```

## Semantics

A Workflow defines a graph of Steps for governed work.
