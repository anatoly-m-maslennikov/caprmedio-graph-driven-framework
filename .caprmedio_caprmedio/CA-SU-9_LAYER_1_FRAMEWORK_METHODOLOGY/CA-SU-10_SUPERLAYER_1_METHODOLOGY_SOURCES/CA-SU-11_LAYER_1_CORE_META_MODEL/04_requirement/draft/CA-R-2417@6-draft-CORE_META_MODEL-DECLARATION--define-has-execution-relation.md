---
atom_id: CA-R-2417
status: Draft
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_EXECUTION
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
version: 6
updated_at: 2026-11-04 16:07:35 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2417@6-draft-CORE_META_MODEL-DECLARATION--define-has-execution-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Define HAS_EXECUTION Relation

## Claim

### Formal Claim

```CFEL
# model
Relation//HAS_EXECUTION <((HAS_INVERSE)) Relation//IS_EXECUTION_OF;

Relation//HAS_EXECUTION ((HAS_CLASSIFICATION)) Derivation == Derived;

# instances
Workflow//$workflow ((HAS_EXECUTION)) Workflow Run//$workflow_run;

Step//$step ((HAS_EXECUTION)) Step Run//$step_run;

Action//$action ((HAS_EXECUTION)) Action Run//$action_run
```

## Semantics

HAS_EXECUTION relates a reusable Workflow, Step or Action to its corresponding actual Run.
