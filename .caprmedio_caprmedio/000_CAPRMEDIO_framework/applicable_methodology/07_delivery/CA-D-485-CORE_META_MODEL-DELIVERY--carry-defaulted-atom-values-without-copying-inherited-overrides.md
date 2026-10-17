---
subjects:
  governs: "Atom Property Default"
  depends_on:
    ["Property", "Atom Property Default", "Entity/Continuant/Object/Atom.Property", "Autonomous Confidence Threshold", "Implementation Retry Limit"]
version: 6
updated_at: "2026-10-15 18:52:22 +0000"
relations: {"relates_to": ["CA-D-478", "CA-D-472", "CA-D-447"]}
atom_id: "CA-D-485"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-485-CORE_META_MODEL-DELIVERY--carry-defaulted-atom-values-without-copying-inherited-overrides.md
  source_atom_id: CA-D-485
  source_atom_revision: 6
  source_sha256: 1e7983142bb55b2316d19ebdaf28572a38e22d23f61cc09b7f89fd3e35f92072
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Carry defaulted Atom values without copying inherited overrides

## Scope

defaulted Atom values and inherited external settings.

## Claim

a writer **must** preserve the distinction between a defaulted Atom Property **and** an inherited external setting:

- a required Atom value selected by applying a default is still carried at its canonical internal location; equality **to** that default does **not** permit omitting the value.
- an unselected optional override remains absent; do **not** copy an inherited effective setting into a locally selected override.
- retain an explicit override even **when** it currently equals the inherited value, because later upstream changes **must not** change that selection.

## Details
