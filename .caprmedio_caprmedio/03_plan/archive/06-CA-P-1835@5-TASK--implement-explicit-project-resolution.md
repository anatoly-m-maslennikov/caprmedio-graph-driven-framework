---
atom_id: CA-P-1835@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 08:22:45 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Project Settings
  - Project Structure
  - Framework Instance Settings
  - Subject/Engineering/Tool
  - Subject/Engineering/Action
  - Workflow Run
  - Subject/Engineering/Carrier
  - Subject/Engineering/Evaluation
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
relations:
  is_decomposition_of:
  - CA-P-1829
  blocks:
  - CA-P-1836
tier: 3
---
# Summary

Implement explicit Project resolution

## Objective

the AI Agent implements the accepted Project selector **and** canonical Framework Instance identity.

## Details

- input: the selection RMED **and** the Project golden tests.
- output: one shared Project-resolution boundary that validates the selected settings/control root, honors the declared authority path, **and** distinguishes two Projects **in** the same repository.
- verification: run the selector cases for unique, explicit, ambiguous, missing, **and** unsafe input; inspect only permitted files **and** paths.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: the shared frozen Project selector **and** derived namespace properties are implemented; all 5 selection tests passed, including distinct nested Project roots, no Git prerequisite, unsafe bindings **and** foreign context refusal.

the Plan is **not** Done **if** ((the selector chooses an unrequested Project) **or** (two selected Projects share an instance identity) **or** (the bounded selector tests fail)).
