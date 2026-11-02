---
subjects:
  governs: Projection Rebuild
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Domain/Node/Continuant/Projection
version: 23
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
atom_id: CA-R-1649@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
status: Archived
author: Anatoly Maslennikov
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
