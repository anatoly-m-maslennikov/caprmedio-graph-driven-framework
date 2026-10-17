---
subjects:
  governs: "Entity/Continuant/Object/Atom"
  depends_on:
    ["Entity/Continuant/Object/Atom.ID", "Entity/Carrier.Canonical Address"]
version: 15
updated_at: "2026-10-16 12:09:20 +0000"
relations: {}
atom_id: "CA-D-336"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-336-CORE_META_MODEL--resolve-active-atoms-from-canonical-carrier-identities.md
  source_atom_id: CA-D-336
  source_atom_revision: 15
  source_sha256: df304f6e2423bfa84ad56e2de387ea04f53f39b565fabd2a3b86dc827bf23c75
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Resolve Active Atoms from Canonical Carrier Identities

## Scope

Active Atom Carrier discovery from selected Project-owned Markdown source frontiers.

## Claim

Active Atom Carrier discovery **must** resolve requested Atom IDs from the identities carried inside the selected Project-owned Markdown source frontier **and** select carried Status Active.

- validate the associated canonical addresses against those internal values under CA-D-480.
- report zero **or** multiple Active matches **and** missing **or** conflicting identity **or** Status; do **not** repair discovery by silently preferring a filename **or** directory.
- a non-Active containing Hub does **not** change the Status of a nested Atom.

## Details
