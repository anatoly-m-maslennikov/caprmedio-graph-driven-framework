---
subjects:
  governs: "Publish Reconciled Projection"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Projection/Type: Reconciled Projection", "Artifact", "Entity/Continuant/Object/Atom.Substance", "Entity/Carrier", "Entity/Continuant/Object/Atom/Content Role: Delivery"]
version: 8
updated_at: "2026-10-18 16:20:19 +0400"
relations: {}
atom_id: "CA-O-009"
content_role: "Operations"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-009-PROJECT_CONFIGURATION-ACTION--publish-reconciled-projections.md
  source_atom_id: CA-O-009
  source_atom_revision: 8
  source_sha256: 9e6eb82c8859a68691315704a4f70d62258145371c2411a07db1e3f6078a2796
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Publish reconciled projections

## Operation

Publish Reconciled Projection **means** the reusable Action that publishes a Reconciled Projection from the exact final selected source Revisions **only** **when** the applicable required checks are complete, no conflict remains unresolved under those checks, **and** required resolution approvals remain valid for that frontier. **before** changing live output, it **must** recheck that the exact current selected sources match the assessed frontier **and** required approval bindings; unresolved **or** indeterminate checks **or** a changed frontier block publication **without** changing that output. it **must** preserve the selected source content, identities, **and** Revisions **without** Claim synthesis **or** merge **and** use the applicable Delivery authority for representation, source traceability, **and** publication. failure **must** be reported **without** claiming a completed publication; prior published state **and** recovery remain governed by applicable authority. the Action does **not** fix source conflicts by editing the result **or** gain source authority through publication.

## Details
