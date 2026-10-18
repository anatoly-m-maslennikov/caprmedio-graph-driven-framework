---
subjects:
  governs: "Artifact.Activity: Active"
  depends_on:
    ["Artifact.Activity", "Artifact.Status"]
version: 11
updated_at: "2026-10-15 12:21:42 +0000"
relations: {}
atom_id: "CA-R-1395"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1395-CORE_META_MODEL-CORE--derive-active-artifact-activity.md
  source_atom_id: CA-R-1395
  source_atom_revision: 11
  source_sha256: 00b0130a6272dd570dd085129083059145ed603b341883dbeb3dd050bd62155f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Active Artifact Activity

## Scope

Artifacts for which Activity applies.

## Claim

an Artifact's Activity **must** be Active **if** Activity applies under CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`=`** Active.

## Details
