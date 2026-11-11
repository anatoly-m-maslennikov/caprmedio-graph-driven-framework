---
atom_id: CA-R-2465
ref_id: CA-R-2465@5-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Step
tier: 3
status: Draft
version: 5
updated_at: 2026-11-05 02:41:45 +0400
carrier_destination:
  file:
    name: CA-R-2465@5-draft-DECLARATION--declare-step.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare Step

## Claim

### Prose Claim

Every Step’s Container chain ends at a Workflow.

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Operations))/Step;

Step ((NARROWER_THAN)) Atom/(.Header.Context.Role in (Operations));

Atom/(.Header.Context.Role in (Operations))/Step >| (Container == yes);

# instances
Step//$step;

$step{::1}((IS_CONTAINED_BY)) (in (Workflow, Step))//$parent;

IF $step {=0}((RUNS)) THEN $step {::1+}((CONTAINS)) Step//$nested_step;

IF $step {>0}((RUNS)) THEN $step {::0}((CONTAINS));

IF $step {=0}((CONTAINS)) THEN $step {::1}((RUNS)) (in (Action, Workflow))//$selected;

Step//$definition {::0+}((HAS_EXECUTION)) Step Run//$run
```

## Semantics

A Step prescribes work within a Workflow.
