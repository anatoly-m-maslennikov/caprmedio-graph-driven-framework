---
subjects:
  governs: "Entity/Node/Continuant/Atom.Status: Archived"
  depends_on:
    - "Entity/Node/Continuant/Atom.Status"
    - "Entity/Node/Continuant/Atom.Version Number"
version: 10
updated_at: "2026-10-20 20:27:54 +0400"
relations: {}
atom_id: "CA-R-1419"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1419-CORE_META_MODEL-CORE--restrict-archived-status-to-non-current-revisions.md
  source_atom_id: CA-R-1419
  source_atom_revision: 10
  source_sha256: cd12f17ccf782923e2bf36f268eda5a5ca705f589ba52fa7721d546b9c8d2c93
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Restrict Archived Status to Non-Current Revisions

## Scope

the Archived Status of an Atom version.

## Claim

an Atom version **may** have Status Archived **only** **if** it is a prior version **or** the final version of a replaced, absorbed, **or** retired Atom.

## Details
