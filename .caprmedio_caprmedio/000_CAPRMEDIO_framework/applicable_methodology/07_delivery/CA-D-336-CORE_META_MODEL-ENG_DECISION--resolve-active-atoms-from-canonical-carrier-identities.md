---
subjects:
  active: Atom
  passive:
  - Atom.ID
  - Carrier.Canonical Address
version: 30
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-336
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-336-CORE_META_MODEL-ENG_DECISION--resolve-active-atoms-from-canonical-carrier-identities.md
  source_atom_id: CA-D-336
  source_atom_revision: 30
  source_sha256: cbb907fde5c830d9f6b7553b02f774ea6863b66477b775a2ed3099b213cbb920
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Resolve Active Atoms from Canonical Carrier Identities

## Claim scope

Active Atom Carrier discovery from selected Project-owned Markdown source frontiers.

## Claim

Active Atom Carrier discovery **must** resolve requested Atom IDs from the identities carried inside the selected Project-owned Markdown source frontier **and** select carried Status Active.

- validate the associated canonical addresses against those internal values under CA-D-480.
- report zero **or** multiple Active matches **and** missing **or** conflicting identity **or** Status; do **not** repair discovery by silently preferring a filename **or** directory.
- a non-Active containing Hub does **not** change the Status of a nested Atom.
