---
atom_id: CA-R-2752
ref_id: CA-R-2752@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Action Run
tier: 3
status: Draft
version: 1
updated_at: 2026-11-05 05:27:06 +0400
carrier_destination:
  file:
    name: CA-R-2752@1-draft-DECLARATION--declare-action-run.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare Action Run

## Claim

### Prose Claim

An Action Run launched by a Step Run is contained by that Step Run.

### Formal Claim

```CFEL
# model
Action Run ((NARROWER_THAN)) Execution;

# instances
Action Run//$run {::1}((IS_EXECUTION_OF)) Action//$definition;

Action Run//$action_run {::0+}((IS_CONTAINED_BY)) Step Run//$step_run
```

## Semantics

An Action Run is an actual execution of one Action.
