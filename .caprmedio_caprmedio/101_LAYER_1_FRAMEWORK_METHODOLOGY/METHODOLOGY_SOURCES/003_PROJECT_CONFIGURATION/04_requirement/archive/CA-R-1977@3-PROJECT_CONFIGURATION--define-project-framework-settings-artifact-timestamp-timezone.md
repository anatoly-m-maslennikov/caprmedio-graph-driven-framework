---
atom_id: CA-R-1977@3
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/Project.Framework Settings.Artifact Timestamp Timezone"
relations:
  child_of:
  - CA-R-1176
version: 3
updated_at: "2026-10-19 15:56:11 +0400"
---
# Summary

Define Project.Framework Settings.Artifact Timestamp Timezone

## Scope

the Artifact timestamp timezone setting in Framework Settings.

## Claim

Artifact Timestamp Timezone **means** the Framework Settings value that supplies the timezone interpretation used when emitting Artifact timestamps.

## Details

Evidence: CA-D-390 supplies the timezone interpretation and its concrete encoding. Candidate #6 keeps Settings attached to Project and keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no format, allowed value or default; those remain separate Delivery rules.
