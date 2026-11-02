---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Reconciled Projection'
  - Subject/Graph Node/Domain/Continuant/Term//Artifact
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Carrier
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-O-009@18
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Action
tier: 3
---
# Summary

Publish reconciled projections

## Operation

Publish Reconciled Projection **means** the reusable Action that publishes a Reconciled Projection from the exact final selected source Revisions **only** **when** the applicable required checks are complete, no conflict remains unresolved under those checks, **and** required resolution approvals remain valid for that frontier. **before** changing live output, it **must** recheck that the exact current selected sources match the assessed frontier **and** required approval bindings; unresolved **or** indeterminate checks **or** a changed frontier block publication **without** changing that output. it **must** preserve the selected source content, identities, **and** Revisions **without** Claim synthesis **or** merge **and** use the applicable Delivery authority for representation, source traceability, **and** publication. failure **must** be reported **without** claiming a completed publication; prior published state **and** recovery remain governed by applicable authority. the Action does **not** fix source conflicts by editing the result **or** gain source authority through publication.

## Details
