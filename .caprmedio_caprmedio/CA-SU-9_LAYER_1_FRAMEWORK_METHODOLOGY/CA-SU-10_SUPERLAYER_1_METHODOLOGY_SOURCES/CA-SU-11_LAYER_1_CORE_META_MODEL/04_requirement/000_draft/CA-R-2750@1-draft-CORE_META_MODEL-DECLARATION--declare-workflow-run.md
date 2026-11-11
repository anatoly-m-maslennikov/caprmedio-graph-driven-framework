---
atom_id: CA-R-2750
ref_id: CA-R-2750@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Workflow Run
tier: 3
status: Draft
version: 1
updated_at: 2026-11-05 05:27:06 +0400
carrier_destination:
  file:
    name: CA-R-2750@1-draft-DECLARATION--declare-workflow-run.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare Workflow Run

## Claim

### Formal Claim

```CFEL
# model
Workflow Run ((NARROWER_THAN)) Execution;

Workflow Run >| (Container == yes);

# instances
Workflow Run//$run {::1}((IS_EXECUTION_OF)) Workflow//$definition;

Workflow Run//$container {::0+}((CONTAINS)) Step Run//$contained_step
```

## Semantics

A Workflow Run is an actual execution of one Workflow with supplied inputs and parameters.
