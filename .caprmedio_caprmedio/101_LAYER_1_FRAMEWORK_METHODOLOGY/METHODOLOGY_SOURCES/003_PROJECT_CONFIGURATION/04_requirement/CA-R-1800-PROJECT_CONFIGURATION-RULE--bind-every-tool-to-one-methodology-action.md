---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Methodology Sources
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering
version: 14
updated_at: 2026-10-27 20:00:03 +0400
relations:
  depends_on:
  - CA-R-1509
atom_id: CA-R-1800
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
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
