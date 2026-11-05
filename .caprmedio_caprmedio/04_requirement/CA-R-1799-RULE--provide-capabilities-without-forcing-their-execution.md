---
atom_id: CA-R-1799
ref_id: CA-R-1799
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
version: 20
updated_at: 2026-11-02 18:35:20 +0400
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
relations:
  child_of:
  - CA-R-2157
tier: 4
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-R-1799-CAPRMEDIO-RULE--provide-capabilities-without-forcing-their-execution.md
    path: .caprmedio_caprmedio/04_requirement
---
## Summary

Provide capabilities **without** forcing their execution

## Claim

### Prose Claim


capabilities provided by the CAPRMEDIO Framework Instance.


the CAPRMEDIO Framework Instance **must** provide capabilities for the Operator **without** initiating **or** forcing their execution independently of Operator authorization.

## Details

- a Requirement **to** provide a capability specifies what is available **to** the Operator; it does **not** itself authorize **or** trigger execution.
- execution follows direct Operator instruction **or** explicit prior authorization. prior authorization **may** cover a Workflow **or** automation **and** its Actions within the authorized targets **and** constraints; separate approval for **every** covered Action is **not** required.
- required outcomes, validation gates, **and** safeguards remain binding **when** an authorized capability executes. capability wording does **not** make those conditions optional.
