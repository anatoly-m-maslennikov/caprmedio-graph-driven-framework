---
subjects:
  governs: "Select Reconciliation Sources"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Projection/Type: Reconciled Projection", "Artifact", "Entity/Continuant/Object/Atom.Substance"]
version: 7
updated_at: "2026-10-15 18:52:39 +0000"
relations: {}
atom_id: "CA-O-004"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-004-CORE_META_MODEL-ACTION--select-reconciliation-sources.md
  source_atom_id: CA-O-004
  source_atom_revision: 7
  source_sha256: d95638d1864bd27a0d10d8990e97c97020b52f1ebb7dc2d7d094300d17836dbe
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Select reconciliation sources

## Operation

Select Reconciliation Sources **means** the reusable Action that resolves the complete source selection required by applicable governing authority **and** returns the exact selected source identities **and** Revisions as one source frontier. it **must** preserve source-selection constraints, include **every** eligible source, **and** retain unresolved selection ambiguity as a reported failure rather than silently choosing **or** discarding a source. selection does **not** change source authority **or** publish a Projection.

## Details
