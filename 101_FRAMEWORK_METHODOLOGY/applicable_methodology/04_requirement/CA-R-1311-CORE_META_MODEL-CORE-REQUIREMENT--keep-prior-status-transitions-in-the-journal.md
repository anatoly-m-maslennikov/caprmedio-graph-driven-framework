---
subjects:
  governs: "Artifact.Status"
  depends_on:
    ["Entity/Node/Continuant/History/Journal"]
version: 16
updated_at: "2026-10-19 15:52:47 +0400"
relations: {}
atom_id: "CA-R-1311"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1311-CORE_META_MODEL-CORE-REQUIREMENT--keep-prior-status-transitions-in-the-journal.md
  source_atom_id: CA-R-1311
  source_atom_revision: 16
  source_sha256: 84395c09423e2f544b32e4e1d1b162c55f5083efbdab30c1005e52fd63e2c37f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Prior Status Transitions in the Journal

## Scope

Artifact Revision Status Properties and their prior transitions.

## Claim

an Artifact Revision **must** expose **only** its current Status as a current Property **and** **must** preserve prior Status transitions through Journal events.

## Details
