---
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Graph Node/Engineering/Methodology
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations'
  - Subject/Graph Node/Engineering/Workflow Orchestration/Action Realization
  - Subject/Graph Node/Engineering
version: 11
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-R-1452
  - CA-R-1509
  - CA-R-1514
  - CA-R-1515
  - CA-R-1517
atom_id: CA-R-1800@11
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Bind **every** Tool to one methodology Action

## Scope

Tools in the caprmedio Project.

## Claim

**in** the caprmedio Project, **every** Tool **must** implement **`=1`** Action defined by an existing applicable methodology O Atom.

## Details

- the Tool's RMED identifies that Action as the behavior it realizes **and** specifies its implementation obligations **without** copying the canonical Action definition.
- a Workflow Step binds its Action under CA-R-1509; the corresponding Tool realizes that Action rather than redefining the Workflow graph.
- this cardinality constrains the Action implemented by the Tool. it does **not** count internal instructions, API calls, interactions, **or** retries.

the binding is **not** a requirement **to** use that Action **or** a particular Workflow **to** build the Tool.
