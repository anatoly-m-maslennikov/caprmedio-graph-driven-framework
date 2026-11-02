---
subjects:
  governs: "Select Reconciliation Sources"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Projection/Type: Reconciled Projection", "Artifact", "Entity/Continuant/Object/Atom.Substance"]
version: 8
updated_at: "2026-10-18 16:19:25 +0400"
relations: {}
atom_id: "CA-O-004"
content_role: "Operations"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
---
# Summary

Select reconciliation sources

## Operation

Select Reconciliation Sources **means** the reusable Action that resolves the complete source selection required by applicable governing authority **and** returns the exact selected source identities **and** Revisions as one source frontier. it **must** preserve source-selection constraints, include **every** eligible source, **and** retain unresolved selection ambiguity as a reported failure rather than silently choosing **or** discarding a source. selection does **not** change source authority **or** publish a Projection.

## Details
