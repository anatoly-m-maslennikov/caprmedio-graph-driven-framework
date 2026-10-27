---
atom_id: CA-R-1799
content_role: Requirement
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: 'Subject/Graph Node/Product: CAPRMEDIO Framework'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
relations:
  child_of:
  - CA-R-2157
tier: 4
type: Rule
---
# Summary

Provide capabilities **without** forcing their execution

## Scope

capabilities provided by the CAPRMEDIO Framework Instance.

## Claim

the CAPRMEDIO Framework Instance **must** provide capabilities for the Operator **without** initiating **or** forcing their execution independently of Operator authorization.

## Details

- a Requirement **to** provide a capability specifies what is available **to** the Operator; it does **not** itself authorize **or** trigger execution.
- execution follows direct Operator instruction **or** explicit prior authorization. prior authorization **may** cover a Workflow **or** automation **and** its Actions within the authorized targets **and** constraints; separate approval for **every** covered Action is **not** required.
- required outcomes, validation gates, **and** safeguards remain binding **when** an authorized capability executes. capability wording does **not** make those conditions optional.
