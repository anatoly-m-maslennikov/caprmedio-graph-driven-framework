---
atom_id: CA-R-1874
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations.Status'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Status
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Extension Sources
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
version: 16
updated_at: 2026-10-27 20:00:05 +0400
relations: {}
tier: 2
type: Rule
---
# Summary

Register Core Operations Status Values

## Scope

the default Status value domain of Operations Atoms with Type Workflow, Step, or Action.

## Claim

the Core allowed values of Operations Status **must** be exactly (Draft, Active, Archived); that one Content Role Status model applies to Operations Atoms with Type Workflow, Step, or Action unless an admitted Extension or Project Configuration establishes a more-specific Status domain under that exact Content Role and Type path.

## Details

this Status is the Artifact Revision Property of the Operations Atom itself. it does **not** define a Status transition, carrier placement, setting, or a Workflow, Step, or Action Run outcome, receipt, retry state, result, or completion state.
