---
subjects:
  governs: "Entity/Continuant/Object/Project.Framework Settings"
  depends_on:
    ["Entity/Continuant/Object/Project.Structure", "Authority Mode", "Entity/Continuant/Object/Project", "Entity/Continuant/Object/Scope Unit"]
version: 9
updated_at: "2026-10-15 18:51:39 +0000"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-374"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-374-CORE_META_MODEL--serialize-instance-authority-mode-selections.md
  source_atom_id: CA-D-374
  source_atom_revision: 9
  source_sha256: e00c3da14fdce0376a89e0319eb032da06c8913a6ba9c43894caa62890f17e31
  original_relations_sha256: dbd41c990ca96026d80a7c6e36e3203724208ce3569ca634233af924bbbfab2f
---
# Summary

Serialize instance Authority Mode selections

## Scope

an explicit Authority Mode selection in the Framework Instance Settings TOML Carrier.

## Claim

an explicit Authority Mode selection **in** the Framework Instance Settings TOML Carrier **must** use `authority_modes.default` for the instance default **or** `authority_modes.project` for the Project override. explicit per-unit overrides **must** use **only** that unit's `authority_mode` **in** authoritative Project Structure; legacy per-unit Settings fields **must not** remain a second selectable source.

## Details
