---
atom_id: CA-R-1799@18
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
version: 18
updated_at: 2026-11-02 00:18:22 +0400
subjects:
  active: 'Entity/Aspect/Product: CAPRMEDIO Framework'
  passive:
  - Entity/Object/Continuant/Actor/Operator
  - Atom/(.Role := Requirement)
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
relations:
  child_of:
  - CA-R-2157
tier: 4
role: Requirement
form: Rule
---
## Summary

Provide capabilities **without** forcing their execution

## Claim scope

capabilities provided by the CAPRMEDIO Framework Instance.

## Claim

the CAPRMEDIO Framework Instance **must** provide capabilities for the Operator **without** initiating **or** forcing their execution independently of Operator authorization.

## Details

- a Requirement **to** provide a capability specifies what is available **to** the Operator; it does **not** itself authorize **or** trigger execution.
- execution follows direct Operator instruction **or** explicit prior authorization. prior authorization **may** cover a Workflow **or** automation **and** its Actions within the authorized targets **and** constraints; separate approval for **every** covered Action is **not** required.
- required outcomes, validation gates, **and** safeguards remain binding **when** an authorized capability executes. capability wording does **not** make those conditions optional.
