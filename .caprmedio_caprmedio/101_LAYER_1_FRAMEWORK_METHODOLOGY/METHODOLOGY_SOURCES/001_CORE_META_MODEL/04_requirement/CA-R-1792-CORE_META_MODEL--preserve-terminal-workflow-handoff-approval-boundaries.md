---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action/Execution Kind'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Execution Context
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 13
updated_at: 2026-10-27 20:00:03 +0400
relations: {}
atom_id: CA-R-1792
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Preserve terminal Workflow handoff approval boundaries

## Scope

a terminal Workflow handoff from an Agentic Step Invocation.

## Claim

a terminal Workflow handoff **must** end the predecessor Run **and** let the executor admit a separate successor under `CA-R-1520-CORE_META_MODEL-GENERAL-REQUIREMENT--return-workflow-handoffs-through-terminal-results`. a session instruction **must not** silently resume an ended Run **or** bypass approval.

## Details
