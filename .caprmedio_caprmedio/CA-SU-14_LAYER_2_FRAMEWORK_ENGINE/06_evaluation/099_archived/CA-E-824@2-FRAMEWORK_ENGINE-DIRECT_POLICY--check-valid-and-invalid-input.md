---
identity:
  atom_id: CA-E-824
  ref_id: CA-E-824@2
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
  version: 2
  status: archived
  updated_at: '2026-11-12T12:29:32.964989+00:00'
destination:
  file:
    name: CA-E-824@2-FRAMEWORK_ENGINE-DIRECT_POLICY--check-valid-and-invalid-input.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/06_evaluation/099_archived
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

Where the operation accepts corrections, check that it returns field errors to the caller, retains valid fields, and accepts corrected fields alone or with additional input. For MCP, check that the AI Agent receives the errors in the response without an Operator form.

Check cancellation at each stage that can wait for correction before a write. Cancellation clears the pending request without applying changes. After a write, check that a failure reports completed effects and ends the request.
