---
atom_id: CA-R-2465
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
version: 4
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2465-CORE_META_MODEL-DECLARATION--declare-step.md
  source_atom_id: CA-R-2465
  source_atom_revision: 4
  source_sha256: 1a5fd2b3245d0045125bf902c2fbdea7c8236f1275f878c020c5cfc797d3fecf
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Step

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Operations)/Step;

# instances
Step//$step;

$step{:1}((IS_CONTAINED_BY)) Workflow//$workflow;

IF $step {=0}((RUNS)) THEN $step {:1+}((CONTAINS)) Substep//$substep;

IF $step {>0}((RUNS)) THEN $step {:0}((CONTAINS));

IF $step {=0}((CONTAINS)) THEN $step {:1}((RUNS)) (in (Action, Workflow))//$selected
```

## Semantics

A Step is a unit of work within a Workflow.
