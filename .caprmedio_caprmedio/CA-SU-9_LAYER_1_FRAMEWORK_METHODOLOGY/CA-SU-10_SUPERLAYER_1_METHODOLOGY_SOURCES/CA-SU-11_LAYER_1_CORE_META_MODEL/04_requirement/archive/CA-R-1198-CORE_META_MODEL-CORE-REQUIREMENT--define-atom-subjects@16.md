---
subjects:
  governs: "Entity/Node/Continuant/Atom.Subjects"
  depends_on:
    ["Entity/Node/Continuant/Atom", "Subject", "GOVERNS", "DEPENDS_ON", "Property", "Entity"]
version: 16
updated_at: "2026-10-19 15:52:36 +0400"
relations: {}
atom_id: "CA-R-1198"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Atom Subjects

## Scope

the Atom Subjects Property.

## Claim

the Atom Subjects Property **means** the Atom Property that records its direct Subject Relations: GOVERNS **and** DEPENDS_ON links from that Atom **to** canonical targets. it preserves the target identities **without** storing copies of the targets **or** introducing a separately identified Subject object **or** a nested Entity **or** Reference Property for **every** link.

## Details
