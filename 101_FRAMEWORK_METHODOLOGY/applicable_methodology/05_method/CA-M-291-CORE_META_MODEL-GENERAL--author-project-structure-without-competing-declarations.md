---
subjects:
  governs: "Entity/Continuant/Object/Project.Structure"
  depends_on:
    ["Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Scope Unit.Name", "Entity/Continuant/Object/Scope Unit/Type", "Entity/Continuant/Object/Scope Unit.Label", "Entity/Continuant/Object/Scope Unit.Local Order", "Entity/Continuant/Object/Scope Unit.Navigational Order Number", "Entity/Continuant/Object/Atom/Content Role: Requirement/Type: Goal", "Entity/Continuant/Object/Project.Framework Settings", "Entity/Carrier"]
version: 8
updated_at: "2026-10-16 12:09:03 +0000"
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
  source_atom_revision: 8
  source_sha256: 3950071d479f3cb4fdda7b4e91d1c4300cb37b9ba77edcb7a99deef913eec728
  original_relations_sha256: 687d41bc387f53992337f6691486ad0c74be07ae4a2bf0a97606f0e0f22a4339
---
# Summary

Author Project Structure **without** competing declarations

## Scope

Project Structure declarations.

## Claim

**to** express Project Structure, use one declaration for **every** non-root Scope Unit, reference its parent by the reserved Project-root reference **or** the parent's unique Name, **and** keep structural Local Order distinct from Navigational Order Number. retain an explicit Label independently of Ordered/Unordered Type. retain readable Structural Level **and** authority path **only** with their checked derivation from declared parentage **and** applicable Carrier conventions; physical nesting **must not** silently replace logical parentage. use concrete Carrier bindings as declared values rather than repeating them **in** Goal, Requirement, **or** Delivery Atoms. write an Authority Mode override **only** **when** explicitly selected for that unit; an omitted override remains inherited rather than copied as an explicit value. references **and** observations **must** distinguish the declared unit from its existing Carrier **and** Goal coverage.

## Details
