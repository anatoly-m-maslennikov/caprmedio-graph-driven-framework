---
atom_id: CA-R-2245
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_EXECUTION_OF
  passive:
  - CAPRMEDIO_MODEL <+ Workflow Run
  - CAPRMEDIO_MODEL <+ Step Run
  - CAPRMEDIO_MODEL <+ Action Run
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action
version: 9
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
updated_at: 2026-11-04 16:07:35 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2245@9-draft-CORE_META_MODEL-DECLARATION--define-is-execution-of-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Define IS_EXECUTION_OF Relation

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_EXECUTION_OF ((HAS_INVERSE)) Relation//HAS_EXECUTION;

Relation//IS_EXECUTION_OF ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Workflow Run//$workflow_run ((IS_EXECUTION_OF)) Workflow//$workflow;

Step Run//$step_run ((IS_EXECUTION_OF)) Step//$step;

Action Run//$action_run ((IS_EXECUTION_OF)) Action//$action
```


## Semantics

IS_EXECUTION_OF relates an actual Workflow Run, Step Run or Action Run to the corresponding reusable definition it executes.
