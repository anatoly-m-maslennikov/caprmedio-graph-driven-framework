---
atom_id: "CA-R-1963@draft"
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: "Draft"
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Relation"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-17 23:25:36 +0000"
---
# Summary

Define Entity/Continuant/Object/Relation

## Scope

typed connections between identified endpoints.

## Claim

a Relation **means** a typed connection between identified endpoints. its admitted kind determines the connection's meaning and direction.

## Details

Candidate #6 retains Relation under Object. CA-R-806 and CA-R-1246 govern Relation Kind metadata and graph-qualified identity; CA-R-1437 governs source authority; CA-R-1472 governs admitted endpoint contexts. This definition adds no Relation Kind, inferred connection or endpoint permission.
