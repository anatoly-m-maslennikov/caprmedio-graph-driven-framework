---
atom_id: CA-E-434
ref_id: CA-E-434@25
container:
  scope_unit: CA-SU-00
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom
tier: 3
relations:
  child_of:
  - CA-E-001
status: archived
version: 25
updated_at: 2026-11-11 05:09:29 +0400
carrier_destination:
  file:
    name: CA-E-434@25-POLICY--evaluate-requirement-checkability.md
    path: .caprmedio_caprmedio/06_evaluation/archive
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
---
## Summary

Evaluate Requirement checkability

## Claim

### Prose Claim


**when** an accepted Requirement is used **to** govern work **or** evaluate a result, its checkability Evaluation **must** return `pass` **if** the available evidence identifies **all** of the following:

- recoverable inputs for checking the Requirement;
- a recoverable check procedure;
- a recoverable interpretation that yields **=1** result **in** (`pass`, `fail`).

**if** **any** of these conditions is missing, the checkability Evaluation **must** return `fail`. satisfying them does **not** require a separate Evaluation Atom **unless** applicable authority requires that Atom for the particular case under CAPRMEDIO-META-REQU-124; an independently governed Evaluation Claim still follows the Atom boundary rules.
