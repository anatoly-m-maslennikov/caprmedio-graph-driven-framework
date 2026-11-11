---
atom_id: CA-R-2464
ref_id: CA-R-2464@7
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow
tier: 3
status: Archived
version: 7
updated_at: '2026-11-11 05:13:50 +0400'
---

## Summary

Declare Workflow

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role := Operations)/Workflow;

Workflow.Header.Form:: [in (Workflow)]{::1};

# instances
Workflow//$workflow{::1+}((CONTAINS)) Step//$step;

Workflow//$workflow_2{::0+}((IS_RUN_BY)) Step//$step_2
```

## Semantics

A Workflow defines a graph of Steps for governed work. Its Purpose distinguishes Runtime Workflows from Project Workflows through the selections `Workflow/(.Purpose := Runtime)` and `Workflow/(.Purpose := Project)`.

Both selections inherit the same Step, Substep and Action definitions, graph rules, bindings and execution model. Steps and Actions can be reused by either selection. Purpose concerns use in a Project; reusable Workflow definitions can serve different Project-relative purposes without copying their canonical definition. Purpose does not determine shared or isolated execution context, definition ownership or delivery location.
