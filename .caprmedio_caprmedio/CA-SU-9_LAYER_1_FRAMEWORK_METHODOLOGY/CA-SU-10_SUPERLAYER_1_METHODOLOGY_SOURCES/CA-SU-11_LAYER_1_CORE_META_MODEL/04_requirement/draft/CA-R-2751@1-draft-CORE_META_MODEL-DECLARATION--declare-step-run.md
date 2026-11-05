---
atom_id: CA-R-2751
ref_id: CA-R-2751@1-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ Step Run
version: 1
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 05:27:06 +0400
carrier_destination:
  file:
    name: CA-R-2751@1-draft-DECLARATION--declare-step-run.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---

## Summary

Declare Step Run

## Claim

### Formal Claim

```CFEL
# model
Step Run ((NARROWER_THAN)) Execution;

Step Run >| (Container == yes);

# instances
Step Run//$run {::1}((IS_EXECUTION_OF)) Step//$definition;

Step Run//$step_run {::1}((IS_CONTAINED_BY)) (in (Workflow Run, Step Run))//$container;

Step Run//$step_parent {::0+}((CONTAINS)) Step Run//$nested_step;

Step Run//$action_parent {::0+}((CONTAINS)) Action Run//$action_run
```

## Semantics

A Step Run is an actual execution of one Step within a Workflow Run.
