---
subjects:
  governs: "Entity/Continuant/Node/Project.Structure"
  depends_on:
    ["Entity/Continuant/Node/Scope Unit", "Entity/Continuant/Node/Scope Unit.Name", "Entity/Continuant/Node/Scope Unit/Type", "Entity/Continuant/Node/Scope Unit.Label", "Entity/Continuant/Node/Scope Unit.Local Order", "Entity/Continuant/Node/Scope Unit.Navigational Order Number", "Entity/Continuant/Node/Atom/Content Role: Requirement/Type: Goal", "Entity/Continuant/Node/Project.Framework Settings", "Entity/Carrier"]
version: 9
updated_at: "2026-10-18 03:34:19 +0400"
relations:
  relates_to:
    - "CA-R-1483"
    - "CA-R-1484"
    - "CA-R-1485"
    - "CA-R-1430"
atom_id: "CA-M-291"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-291-CORE_META_MODEL-GENERAL--author-project-structure-without-competing-declarations.md
  source_atom_id: CA-M-291
  source_atom_revision: 9
  source_sha256: c663a71ae78183f54502f99e4de3d77316667eca5fb5f46bb40d044740b20850
  original_relations_sha256: 687d41bc387f53992337f6691486ad0c74be07ae4a2bf0a97606f0e0f22a4339
---
# Summary

Author Project Structure **without** competing declarations

## Scope

Project Structure declarations.

## Claim

**to** express Project Structure, use one declaration for **every** non-root Scope Unit, reference its parent by the reserved Project-root reference **or** the parent's unique Name, **and** keep structural Local Order distinct from Navigational Order Number. retain an explicit Label independently of Ordered/Unordered Type. retain readable Structural Level **and** authority path **only** with their checked derivation from declared parentage **and** applicable Carrier conventions; physical nesting **must not** silently replace logical parentage. use concrete Carrier bindings as declared values rather than repeating them **in** Goal, Requirement, **or** Delivery Atoms. write an Authority Mode override **only** **when** explicitly selected for that unit; an omitted override remains inherited rather than copied as an explicit value. references **and** observations **must** distinguish the declared unit from its existing Carrier **and** Goal coverage.

## Details
