---
subjects:
  governs: "Entity/Node/Continuant/Project.Structure"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Scope Unit.Name", "Entity/Node/Continuant/Scope Unit/Type", "Entity/Node/Continuant/Scope Unit.Label", "Entity/Node/Continuant/Scope Unit.Local Order", "Entity/Node/Continuant/Scope Unit.Navigational Order Number", "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Goal", "Entity/Node/Continuant/Project.Framework Settings", "Entity/Carrier"]
version: 10
updated_at: "2026-10-19 15:54:47 +0400"
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
  source_atom_revision: 10
  source_sha256: 7b1f6c1a9d7dffa1a43d1d7dfd32fc15b474df6e33b4bd6cc289e7a34585474a
  original_relations_sha256: 687d41bc387f53992337f6691486ad0c74be07ae4a2bf0a97606f0e0f22a4339
---
# Summary

Author Project Structure **without** competing declarations

## Scope

Project Structure declarations.

## Claim

**to** express Project Structure, use one declaration for **every** non-root Scope Unit, reference its parent by the reserved Project-root reference **or** the parent's unique Name, **and** keep structural Local Order distinct from Navigational Order Number. retain an explicit Label independently of Ordered/Unordered Type. retain readable Structural Level **and** authority path **only** with their checked derivation from declared parentage **and** applicable Carrier conventions; physical nesting **must not** silently replace logical parentage. use concrete Carrier bindings as declared values rather than repeating them **in** Goal, Requirement, **or** Delivery Atoms. write an Authority Mode override **only** **when** explicitly selected for that unit; an omitted override remains inherited rather than copied as an explicit value. references **and** observations **must** distinguish the declared unit from its existing Carrier **and** Goal coverage.

## Details
