---
subjects:
  governs: Publish Reconciled Projection
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Projection/Type: Reconciled Projection'
  - Artifact
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
version: 12
updated_at: 2026-10-23 03:20:06 +0400
relations: {}
atom_id: CA-O-009@12
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
type: Action
global_tier: 11
---
# Summary

Publish reconciled projections

## Operation

Publish Reconciled Projection **means** the reusable Action that publishes a Reconciled Projection from the exact final selected source Revisions **only** **when** the applicable required checks are complete, no conflict remains unresolved under those checks, **and** required resolution approvals remain valid for that frontier. **before** changing live output, it **must** recheck that the exact current selected sources match the assessed frontier **and** required approval bindings; unresolved **or** indeterminate checks **or** a changed frontier block publication **without** changing that output. it **must** preserve the selected source content, identities, **and** Revisions **without** Claim synthesis **or** merge **and** use the applicable Delivery authority for representation, source traceability, **and** publication. failure **must** be reported **without** claiming a completed publication; prior published state **and** recovery remain governed by applicable authority. the Action does **not** fix source conflicts by editing the result **or** gain source authority through publication.

## Details
