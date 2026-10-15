---
subjects:
  governs: "Entity/Continuant/Object/Atom.Governed Subject"
  depends_on:
    ["Entity/Continuant/Object/Atom.Subjects", "GOVERNS", "Subject", "Relation Kind", "Entity", "Entity/Continuant/Object/Atom.Substance"]
version: 14
updated_at: "2026-10-15 18:42:13 +0000"
relations:
  child_of:
    - CA-R-1269
    - CA-R-1199
    - CA-R-1201
    - CA-R-1202
atom_id: "CA-R-1363"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Atom Governed Subject

## Scope

an Atom's governed Subject relation.

## Claim

an Atom Governed Subject **means** the Atom's **`=1`** Subject Relation whose Relation Kind is GOVERNS. its target is the canonical Entity governed by the Atom's Claim; the Relation **and** its target are distinct.

## Details
