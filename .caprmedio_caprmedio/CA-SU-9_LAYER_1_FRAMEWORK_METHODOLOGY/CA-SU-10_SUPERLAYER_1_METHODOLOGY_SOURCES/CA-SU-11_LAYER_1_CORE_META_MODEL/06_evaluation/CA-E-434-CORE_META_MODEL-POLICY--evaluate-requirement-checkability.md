---
atom_id: CA-E-434
ref_id: CA-E-434
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom
tier: 3
relations:
  child_of:
  - CA-E-001
status: Active
version: 26
updated_at: 2026-11-11 06:01:45 +0400
carrier_destination:
  file:
    name: CA-E-434-CORE_META_MODEL-POLICY--evaluate-requirement-checkability.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Evaluate Requirement checkability

## Claim

### Prose Claim


**when** an accepted Requirement is used **to** govern work **or** evaluate a result, its checkability Evaluation **must** return `pass` **if** the available evidence identifies **all** of the following:

- recoverable inputs for checking the Requirement;
- a recoverable check procedure;
- a recoverable interpretation that yields **=1** result **in** (`pass`, `fail`).

**if** **any** of these conditions is missing, the checkability Evaluation **must** return `fail`. satisfying them does **not** require a separate Evaluation Atom **unless** applicable authority requires that Atom for the particular case under CA-R-1707; an independently governed Evaluation Claim still follows the Atom boundary rules.
