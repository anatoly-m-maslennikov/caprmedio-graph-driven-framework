---
atom_id: CA-O-080@16
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Carrier
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Check Atoms Step'
version: 16
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
---
# Summary

Validate Atom Carriers

## Operation

Atom Carrier Validation **means** the reusable Workflow with the following graph; the referenced Step owns its invocation binding.

- entry **and** sole node: CA-O-088.
- terminal results end the Workflow Run **and** are **not** Steps.

| From Step | Result condition | Terminal result |
|---|---|---|
| CA-O-088 | valid | valid |
| CA-O-088 | invalid | invalid |
| CA-O-088 | incomplete | incomplete |
| CA-O-088 | error | error |

an undeclared result **or** failed Step invocation ends the Run as `error` with available partial evidence. the graph has no back edge, automatic retry, repair, **or** successor-Workflow invocation.

## Details
