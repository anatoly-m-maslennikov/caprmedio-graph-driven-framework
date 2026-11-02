---
subjects:
  governs: "Artifact.Activity"
  depends_on:
    ["Artifact", "Artifact.Status"]
version: 13
updated_at: "2026-10-15 12:21:24 +0000"
relations: {}
atom_id: "CA-R-1307"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models.md
  source_atom_id: CA-R-1307
  source_atom_revision: 13
  source_sha256: 10fb045b3e12f0642f29c08ea49d9c4d4213d9dc70ecdb3edb2403aa99cf5d5f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Limit Artifact Activity to explicit Status models

## Scope

Artifacts to which explicitly defined Status models apply.

## Claim

an Artifact **must** have **`=1`** Activity **in** (Active, Inactive) **if** an explicitly defined Status model applies **to** it, **and** **`=0`** Activity **otherwise**.

## Details
