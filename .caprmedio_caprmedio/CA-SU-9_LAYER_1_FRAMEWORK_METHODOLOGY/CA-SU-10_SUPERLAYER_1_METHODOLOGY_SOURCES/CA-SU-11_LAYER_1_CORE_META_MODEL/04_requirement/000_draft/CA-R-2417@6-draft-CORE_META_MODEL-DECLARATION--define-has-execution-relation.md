---
atom_id: CA-R-2417
ref_id: CA-R-2417@6-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_EXECUTION
tier: 1
status: Draft
version: 6
updated_at: 2026-11-04 16:07:35 +0400
carrier_destination:
  file:
    name: CA-R-2417@6-draft-CORE_META_MODEL-DECLARATION--define-has-execution-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Define HAS_EXECUTION Relation

## Claim

### Formal Claim

```python
# model
relation(source='Relation//HAS_EXECUTION', name='HAS_INVERSE', target='Relation//IS_EXECUTION_OF', reverse=True)
classify(address='Relation//HAS_EXECUTION', axis='Derivation', value='Derived', notation='relation')
# instances
relation(source='Workflow//$workflow', name='HAS_EXECUTION', target='Workflow Run//$workflow_run')
relation(source='Step//$step', name='HAS_EXECUTION', target='Step Run//$step_run')
relation(source='Action//$action', name='HAS_EXECUTION', target='Action Run//$action_run')
```

## Semantics

HAS_EXECUTION relates a reusable Workflow, Step or Action to its corresponding actual Run.
