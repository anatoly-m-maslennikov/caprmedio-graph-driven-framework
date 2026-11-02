---
atom_id: CA-R-1971
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Occurrent/Session"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-19 15:54:14 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1971-CORE_META_MODEL--define-entity-occurrent-session.md
  source_atom_id: CA-R-1971
  source_atom_revision: 2
  source_sha256: 85bce9e984da2aff28876888769af23d6b48544279d56ec39bfe61b697d59602
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Entity/Occurrent/Session

## Scope

Sessions as Occurrents.

## Claim

a Session **means** actual ongoing interaction, **not** a session log **or** a stored session-state envelope.

## Details

The approved model places actual Sessions under Occurrent and distinguishes them from their logs. Candidate #6 preserves that branch. CA-R-1650 governs the bounded session-state envelope, not the actual Session.

 No active Session definition was found in the reviewed sources.
