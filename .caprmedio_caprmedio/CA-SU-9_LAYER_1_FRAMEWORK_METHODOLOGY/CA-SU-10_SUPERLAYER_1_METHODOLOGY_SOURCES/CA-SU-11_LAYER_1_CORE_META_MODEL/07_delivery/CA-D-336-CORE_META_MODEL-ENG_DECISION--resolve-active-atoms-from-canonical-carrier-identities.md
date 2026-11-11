---
atom_id: CA-D-336
ref_id: CA-D-336
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Identity.ID
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 31
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-336-CORE_META_MODEL-DECISION--resolve-active-atoms-from-canonical-carrier-identities.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Resolve Active Atoms from Canonical Carrier Identities

## Claim

### Prose Claim


Active Atom Carrier discovery from selected Project-owned Markdown source frontiers.


Active Atom Carrier discovery **must** resolve requested Atom IDs from the identities carried inside the selected Project-owned Markdown source frontier **and** select carried Status Active.

- validate the associated canonical addresses against those internal values under CA-D-480.
- report zero **or** multiple Active matches **and** missing **or** conflicting identity **or** Status; do **not** repair discovery by silently preferring a filename **or** directory.
- a non-Active containing Hub does **not** change the Status of a nested Atom.
