---
atom_id: CA-R-2464
ref_id: CA-R-2464@6-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Workflow
tier: 3
status: Draft
version: 6
updated_at: '2026-11-11 05:13:50 +0400'
carrier_destination:
  file:
    name: CA-R-2464@6-draft-DECLARATION--declare-workflow.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare Workflow

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Operations))/Workflow;

Workflow ((NARROWER_THAN)) Atom/(.Header.Context.Role in (Operations));

Workflow.Header.Context.Form:: [in (Workflow)]{::1};

Atom/(.Header.Context.Role in (Operations))/Workflow >| (Container == yes);

# instances
Workflow//$workflow{::1+}((CONTAINS)) Step//$step;

Workflow//$workflow_2{::0+}((IS_RUN_BY)) Step//$step_2;

Workflow//$definition {::0+}((HAS_EXECUTION)) Workflow Run//$run
```

## Semantics

A Workflow defines a graph of Steps for governed work. Its Purpose distinguishes Runtime Workflows from Project Workflows through the selections `Workflow/(.Purpose := Runtime)` and `Workflow/(.Purpose := Project)`.

Both selections inherit the same Step and Action definitions, graph rules, bindings and execution model. Steps and Actions can be reused by either selection. Purpose concerns use in a Project; reusable Workflow definitions can serve different Project-relative purposes without copying their canonical definition. Purpose does not determine shared or isolated execution context, definition ownership or delivery location.
