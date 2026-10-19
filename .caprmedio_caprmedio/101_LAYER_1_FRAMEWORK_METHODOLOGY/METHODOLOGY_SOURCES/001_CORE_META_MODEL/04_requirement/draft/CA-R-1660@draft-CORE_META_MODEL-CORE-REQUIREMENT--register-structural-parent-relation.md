---
subjects:
  governs: "Structural Parent Relation"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Project.Structure", "Structural Entity"]
version: 19
updated_at: "2026-10-19 11:41:56 +0000"
relations: {}
atom_id: "CA-R-1660@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Register structural parent relation

## Scope

the Structural Parent Relation directed from a child to its immediate parent.

## Claim

the Structural Parent Relation **must** be the kind-independent Structural ownership relation directed from a child **to** its immediate parent. Project Structure owns Scope Unit parent declarations; structural graph views derive the corresponding `structural_parent` edge **without** maintaining a second source. a Carrier's physical containment **must not** silently replace a declared logical parent.

## Details
