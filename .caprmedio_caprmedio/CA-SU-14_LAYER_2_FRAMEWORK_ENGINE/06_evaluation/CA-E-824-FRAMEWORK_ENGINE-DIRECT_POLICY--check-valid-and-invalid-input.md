---
identity:
  atom_id: CA-E-824
  ref_id: CA-E-824
context:
  role: evaluation
  form: direct_policy
  tier: 3
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Verification <+ Test Design
  container:
    scope_unit: CA-SU-14
state:
  version: 1
  status: active
  updated_at: '2026-11-11T17:28:27.098061+00:00'
destination:
  file:
    name: CA-E-824-FRAMEWORK_ENGINE-DIRECT_POLICY--check-valid-and-invalid-input.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/06_evaluation
---
## Summary

Check valid and invalid input

## Claim

### Prose Claim

Check how an Engine operation behaves with each applicable input case.
- valid input.
- valid fields and one or more wrong values.
- valid fields and one or more missing required values.
- wrong and missing values together when both can occur in one request.

Where the operation accepts corrections, check that valid fields are retained and that submitting only the requested corrections can complete the operation.
