---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.ID
  - Subject/Graph Node/Engineering/Continuant/Carrier.Canonical Address
version: 24
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-D-336@24
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
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
