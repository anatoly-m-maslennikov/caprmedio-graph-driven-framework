---
subjects:
  governs: "Entity/Node/Continuant/Atom.Governed Subject"
  depends_on:
    ["Entity/Node/Continuant/Atom.Subjects", "GOVERNS", "Subject", "Relation Kind", "Subject Target", "Entity/Node/Continuant/Atom.Substance"]
version: 16
updated_at: "2026-10-21 01:47:52 +0400"
relations:
  child_of:
    - CA-R-1269
    - CA-R-1199
    - CA-R-1201
    - CA-R-1202
atom_id: "CA-R-1363@16"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Archived"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Atom Governed Subject

## Scope

an Atom's governed Subject relation.

## Claim

an Atom Governed Subject **means** the Atom's **`=1`** Subject Relation whose Relation Kind is GOVERNS. its target is the canonical Subject Target governed by the Atom's Claim; the Relation **and** its target are distinct.

## Details
