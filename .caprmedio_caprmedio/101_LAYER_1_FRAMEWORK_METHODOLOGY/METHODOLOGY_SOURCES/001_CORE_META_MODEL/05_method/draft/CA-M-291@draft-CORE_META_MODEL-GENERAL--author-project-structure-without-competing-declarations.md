---
subjects:
  governs: "Entity/Node/Continuant/Project.Structure"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Scope Unit.Name", "Entity/Node/Continuant/Scope Unit/Type", "Entity/Node/Continuant/Scope Unit.Label", "Entity/Node/Continuant/Scope Unit.Local Order", "Entity/Node/Continuant/Scope Unit.Navigational Order Number", "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Goal", "Entity/Node/Continuant/Project.Framework Settings", "Entity/Carrier"]
version: 10
updated_at: "2026-10-19 11:44:19 +0000"
relations:
  relates_to:
    - "CA-R-1483"
    - "CA-R-1484"
    - "CA-R-1485"
    - "CA-R-1430"
atom_id: "CA-M-291@draft"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Author Project Structure **without** competing declarations

## Scope

Project Structure declarations.

## Claim

**to** express Project Structure, use one declaration for **every** non-root Scope Unit, reference its parent by the reserved Project-root reference **or** the parent's unique Name, **and** keep structural Local Order distinct from Navigational Order Number. retain an explicit Label independently of Ordered/Unordered Type. retain readable Structural Level **and** authority path **only** with their checked derivation from declared parentage **and** applicable Carrier conventions; physical nesting **must not** silently replace logical parentage. use concrete Carrier bindings as declared values rather than repeating them **in** Goal, Requirement, **or** Delivery Atoms. write an Authority Mode override **only** **when** explicitly selected for that unit; an omitted override remains inherited rather than copied as an explicit value. references **and** observations **must** distinguish the declared unit from its existing Carrier **and** Goal coverage.

## Details
