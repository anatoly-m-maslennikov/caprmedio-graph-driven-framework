---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Projection
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Domain/Continuant/Projection
version: 29
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1649@29
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Journal Projection Rebuild Events

## Scope

Projection Rebuilds and their Work Journal Actions and terminal Events.

## Claim

**every** Projection Rebuild **must** have **`=1`** Work Journal Action whose terminal Event records the rebuild outcome.

## Details

acceptance of that Event into the Journal does **not**, by itself, make the Projection current. currentness remains subject **to** the Projection's applicable source **and** validation requirements; the accepted Event preserves the observed outcome **without** replacing those requirements.
