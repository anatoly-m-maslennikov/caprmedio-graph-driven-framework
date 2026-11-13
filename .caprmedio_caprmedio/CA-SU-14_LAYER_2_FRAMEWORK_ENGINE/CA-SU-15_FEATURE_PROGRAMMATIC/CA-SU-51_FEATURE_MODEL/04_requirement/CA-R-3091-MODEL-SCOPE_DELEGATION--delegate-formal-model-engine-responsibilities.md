---
identity:
  atom_id: CA-R-3091
  ref_id: CA-R-3091
context:
  role: requirement
  form: scope_delegation
  tier: 3
  container:
    scope_unit: CA-SU-51
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FORMAL_MODEL_ENGINE
state:
  version: 3
  status: active
  updated_at: '2026-11-13T15:38:20.545921+00:00'
destination:
  file:
    name: CA-R-3091-MODEL-SCOPE_DELEGATION--delegate-formal-model-engine-responsibilities.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-51_FEATURE_MODEL/04_requirement
---
## Summary

Delegate formal Model engine responsibilities

## Claim

### Prose Claim

The receiving Scope Unit is FORMAL_MODEL_ENGINE. The admitted HAS_ACTIVE_SUBJECT target is exactly the declared instance at this address:

- `CAPRMEDIO_STRUCTURE <+ Scope Unit//FORMAL_MODEL_ENGINE`.

Existing global default admissions remain unchanged. No additional Role/Form pairs are granted.

- Read the Model Declarations and check their Python Formal Claims for syntax and references.
- Validate the complete Model, including inheritance and Relation contracts.
- Build GENERATED_MODEL from the verified Python Formal Claims. The Formal Claims are the Model rules.

The first build uses Declarations in `CAPRMEDIO_MODEL`. Resolve `NARROWER_THAN` as Python class inheritance during the build.
