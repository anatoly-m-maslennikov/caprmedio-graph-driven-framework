---
subjects:
  governs: "Entity/Node/Continuant/Relation"
  depends_on:
    ["Entity/Node/Continuant/Projection", "Entity/Node/Continuant/Atom", "Entity/Node", "Entity/Node/Continuant/History/Journal", "Entity/Relation"]
version: 9
updated_at: "2026-10-20 12:30:27 +0000"
relations: {}
atom_id: "CA-R-1472@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Admit typed secondary graph connections

## Scope

connections represented by a secondary CAPRMEDIO Graph.

## Claim

a secondary CAPRMEDIO Graph **may** represent typed Relations between its own nodes, **to** another secondary graph **or** its nodes, **and** **to** source Atoms **or** other admitted authoritative sources.

**every** connection **must** use **`=1`** graph-qualified Relation Kind whose governing authority admits its endpoint classes, endpoint graph contexts, direction, **and** cardinality. crossing a graph boundary **must not** transfer Relation Kind ownership, import a foreign Relation Kind as native, **or** make a referenced external endpoint a native node of the receiving graph. a cross-graph reference preserves the referenced identity **without** copying its source fact into independent authority. these permissions do **not** admit concrete Relation Kinds **or** authorize inference beyond their declared rules.

## Details
