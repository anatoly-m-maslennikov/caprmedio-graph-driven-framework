---
atom_id: CA-R-1944
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Continuant/Actor.Name
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:40:40 +0400"
---
# Summary

Define Actor.Name

## Scope

Actor names.

## Claim

Actor.Name **means** the optional name of an Actor.

## Details

Candidate #5 makes Actor.Name optional and inherited by Actor Types; Candidate #6 retains Actor as a Continuant. CA-R-1422 defines Operator and CA-R-1552 governs AI Agent permissions, but neither defines this shared property. This draft does not make Name mandatory or prescribe its storage.
