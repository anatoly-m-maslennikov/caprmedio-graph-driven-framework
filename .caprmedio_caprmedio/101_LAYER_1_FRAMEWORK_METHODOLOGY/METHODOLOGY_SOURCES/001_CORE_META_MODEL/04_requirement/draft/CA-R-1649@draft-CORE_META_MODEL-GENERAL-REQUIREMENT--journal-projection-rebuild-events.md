---
subjects:
  governs: "Projection Rebuild"
  depends_on:
    ["Entity/Node/Continuant/History/Journal.Record", "Entity/Node/Continuant/Projection"]
version: 22
updated_at: "2026-10-19 11:41:56 +0000"
relations: {}
atom_id: "CA-R-1649@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Journal Projection Rebuild Events

## Scope

Projection Rebuilds and their Work Journal Actions and terminal Events.

## Claim

**every** Projection Rebuild **must** have **`=1`** Work Journal Action whose terminal Event records the rebuild outcome.

## Details

acceptance of that Event into the Journal does **not**, by itself, make the Projection current. currentness remains subject **to** the Projection's applicable source **and** validation requirements; the accepted Event preserves the observed outcome **without** replacing those requirements.
