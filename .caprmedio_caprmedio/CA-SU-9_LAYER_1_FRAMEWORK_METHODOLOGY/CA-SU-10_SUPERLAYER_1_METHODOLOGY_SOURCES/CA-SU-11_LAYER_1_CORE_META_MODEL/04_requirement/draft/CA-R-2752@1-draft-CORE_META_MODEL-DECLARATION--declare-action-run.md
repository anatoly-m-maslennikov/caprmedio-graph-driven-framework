---
atom_id: CA-R-2752
ref_id: CA-R-2752@1-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ Action Run
version: 1
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 05:27:06 +0400
carrier_destination:
  file:
    name: CA-R-2752@1-draft-DECLARATION--declare-action-run.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---

## Summary

Declare Action Run

## Claim

### Formal Claim

```CFEL
# model
Action Run ((NARROWER_THAN)) Execution;

# instances
Action Run//$run {::1}((IS_EXECUTION_OF)) Action//$definition;

Action Run//$action_run {::0+}((IS_CONTAINED_BY)) Step Run//$step_run
```

### Prose Claim

An Action Run launched by a Step Run is contained by that Step Run.

## Semantics

An Action Run is an actual execution of one Action.
