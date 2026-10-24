---
atom_id: CA-O-080
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph/Relation/Type: On Result'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step//Check Atoms Step'
version: 12
updated_at: 2026-10-24 00:51:05 +0400
relations:
  relates_to:
  - CA-O-088
  - CA-R-1513
  - CA-R-1519
  - CA-R-1570
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
