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
---
# Summary

Restrict Archived Status to Non-Current Revisions

## Scope

the Archived Status of an Atom version.

## Claim

an Atom version **may** have Status Archived **only** **if** it is a prior version **or** the final version of a replaced, absorbed, **or** retired Atom.

## Details
