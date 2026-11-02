---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Concern.Priority"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role", "Entity/Node/Continuant/Atom/Content Role: Concern.Priority", "Entity/Node/Continuant/Atom/Content Role: Plan"]
version: 12
updated_at: "2026-10-19 15:55:40 +0400"
relations: {}
atom_id: "CA-D-386"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-386-CORE_META_MODEL-DELIVERY--serialize-concern-priority.md
  source_atom_id: CA-D-386
  source_atom_revision: 12
  source_sha256: 5e67b964b21618329f81dfebf0dc6b6386761d76c778a1b64998a02d9fc0f7ac
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Concern Priority

## Scope

Concern Atom Carriers and non-Concern Content Role Atom Carriers.

## Claim

a Concern Atom Carrier **must** serialize **`=1`** selected Priority as `priority` with the lowercase value `high`, `medium`, **or** `low`. **every** non-Concern Content Role Atom Carrier **must** omit `priority`; virtual `highest` **must not** be stored.

## Details
