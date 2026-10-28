---
atom_id: CA-R-1874@15
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations.Status'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type'
  - Subject/Graph Node/Domain/Continuant/Atom.Status
  - Subject/Graph Node/Domain/Continuant/Selection//Extension Sources
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
version: 15
updated_at: 2026-10-26 05:59:45 +0400
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
