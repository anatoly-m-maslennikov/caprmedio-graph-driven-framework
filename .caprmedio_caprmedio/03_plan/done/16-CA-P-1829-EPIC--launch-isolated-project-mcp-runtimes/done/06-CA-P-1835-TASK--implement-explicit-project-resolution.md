---
atom_id: CA-P-1835
ref_id: CA-P-1835
container:
  atom: CA-P-1829
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/MCP
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Engineering/Evaluation
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1829
  blocks:
  - CA-P-1836
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 6-CA-P-1835-TASK--implement-explicit-project-resolution.md
    path: .caprmedio_caprmedio/03_plan/done/16-CA-P-1829-EPIC--launch-isolated-project-mcp-runtimes/done
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
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
