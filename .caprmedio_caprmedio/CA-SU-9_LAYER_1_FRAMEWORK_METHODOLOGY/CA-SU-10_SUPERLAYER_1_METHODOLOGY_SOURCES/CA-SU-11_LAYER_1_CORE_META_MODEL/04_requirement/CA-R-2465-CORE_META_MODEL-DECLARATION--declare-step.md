---
atom_id: CA-R-2465
ref_id: CA-R-2465
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Step
tier: 3
status: Active
version: 6
updated_at: '2026-11-11 16:04:42 +0400'
carrier_destination:
  file:
    name: CA-R-2465-CORE_META_MODEL-DECLARATION--declare-step.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Step

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Operations))/Step;

Step ((NARROWER_THAN)) Atom/(.Header.Context.Role in (Operations));

# instances
Step//$step;

$step{::1}((IS_CONTAINED_BY)) Workflow//$workflow;

IF $step {=0}((RUNS)) THEN $step {::1+}((CONTAINS)) Substep//$substep;

IF $step {>0}((RUNS)) THEN $step {::0}((CONTAINS));

IF $step {=0}((CONTAINS)) THEN $step {::1}((RUNS)) (in (Action, Workflow))//$selected
```

## Semantics

A Step is a unit of work within a Workflow.
