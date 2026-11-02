---
subjects:
  governs: "Select Reconciliation Sources"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Projection/Type: Reconciled Projection", "Artifact", "Entity/Node/Continuant/Atom.Substance"]
version: 9
updated_at: "2026-10-19 15:56:26 +0400"
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
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-004-PROJECT_CONFIGURATION-ACTION--select-reconciliation-sources.md
  source_atom_id: CA-O-004
  source_atom_revision: 9
  source_sha256: 5426cd2321957b0f52a45e577ceea8267f70c69b587e3ff7c6b21319f26b7ab8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Select reconciliation sources

## Operation

Select Reconciliation Sources **means** the reusable Action that resolves the complete source selection required by applicable governing authority **and** returns the exact selected source identities **and** Revisions as one source frontier. it **must** preserve source-selection constraints, include **every** eligible source, **and** retain unresolved selection ambiguity as a reported failure rather than silently choosing **or** discarding a source. selection does **not** change source authority **or** publish a Projection.

## Details
