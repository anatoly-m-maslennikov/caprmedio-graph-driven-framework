---
subjects:
  governs: "Entity/Node/Continuant/Atom.Subjects"
  depends_on:
    - "Relation Kind"
    - "GOVERNS"
    - "DEPENDS_ON"
version: 13
updated_at: "2026-10-19 11:39:04 +0000"
relations: {}
atom_id: "CA-R-1276@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Type Every Direct Subject Reference

## Scope

direct references in an Atom's Subjects Property.

## Claim

**every** direct reference **in** an Atom's Subjects Property **must** use **`=1`** Relation Kind **in** (GOVERNS, DEPENDS_ON). the relation entry supplies this kind **without** an additional kind Property on a Subject object.

## Details
