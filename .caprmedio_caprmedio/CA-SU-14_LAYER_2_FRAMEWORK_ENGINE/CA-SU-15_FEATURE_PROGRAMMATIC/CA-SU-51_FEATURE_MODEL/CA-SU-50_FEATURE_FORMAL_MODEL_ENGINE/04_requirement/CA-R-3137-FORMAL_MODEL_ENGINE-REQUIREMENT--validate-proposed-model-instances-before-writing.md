---
identity:
  atom_id: CA-R-3137
  ref_id: CA-R-3137
context:
  role: requirement
  form: requirement
  tier: 3
  container:
    scope_unit: CA-SU-50
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FORMAL_MODEL_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-13T15:38:33.283869+00:00'
destination:
  file:
    name: CA-R-3137-FORMAL_MODEL_ENGINE-REQUIREMENT--validate-proposed-model-instances-before-writing.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-51_FEATURE_MODEL/CA-SU-50_FEATURE_FORMAL_MODEL_ENGINE/04_requirement
---
## Summary

Validate proposed Model instances before writing

## Claim

### Prose Claim

Before writing a new or updated instance, validate the complete proposed instance against all applicable Model rules, including inherited rules. Reject undeclared Properties, incorrect value types, values outside the allowed set, and violations of cardinality or Relation constraints.

In a batch, validate each target before its write in the existing execution order. Write the first validation error to stderr and stop the operation. Earlier successful writes remain applied.
