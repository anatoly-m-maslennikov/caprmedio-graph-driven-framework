---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Name
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit/Type
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Label
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Local Order
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Navigational Order Number
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Goal'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - Subject/CAPRMEDIO/Carrier
version: 20
updated_at: 2026-10-27 19:59:41 +0400
relations: {}
atom_id: CA-M-291
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Implementation Method
---
# Summary

Author Project Structure **without** competing declarations

## Scope

Project Structure declarations.

## Claim

**to** express Project Structure, use one declaration for **every** non-root Scope Unit, reference its parent by the reserved Project-root reference **or** the parent's unique Name, **and** keep structural Local Order distinct from Navigational Order Number. retain an explicit Label independently of Ordered/Unordered Type. retain a readable derived Scope Unit Path **only** with its checked derivation from declared parentage **and** applicable Carrier conventions; do not author or persist Structural Level, and physical nesting **must not** silently replace logical parentage. use concrete Carrier bindings as declared values rather than repeating them **in** Goal, Requirement, **or** Delivery Atoms. write an Authority Mode override **only** **when** explicitly selected for that unit; an omitted override remains inherited rather than copied as an explicit value. references **and** observations **must** distinguish the declared unit from its existing Carrier **and** Goal coverage.

## Details
