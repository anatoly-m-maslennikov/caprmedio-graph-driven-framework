---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Structure
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Scope Unit.Name
  - Subject/Domain/Node/Continuant/Scope Unit/Type
  - Subject/Domain/Node/Continuant/Scope Unit.Label
  - Subject/Domain/Node/Continuant/Scope Unit.Local Order
  - Subject/Domain/Node/Continuant/Scope Unit.Navigational Order Number
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Goal'
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Engineering/Carrier
version: 14
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-R-1483
  - CA-R-1484
  - CA-R-1485
  - CA-R-1430
atom_id: CA-M-291@14
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
---
# Summary

Author Project Structure **without** competing declarations

## Scope

Project Structure declarations.

## Claim

**to** express Project Structure, use one declaration for **every** non-root Scope Unit, reference its parent by the reserved Project-root reference **or** the parent's unique Name, **and** keep structural Local Order distinct from Navigational Order Number. retain an explicit Label independently of Ordered/Unordered Type. retain a readable derived Scope Unit Path **only** with its checked derivation from declared parentage **and** applicable Carrier conventions; do not author or persist Structural Level, and physical nesting **must not** silently replace logical parentage. use concrete Carrier bindings as declared values rather than repeating them **in** Goal, Requirement, **or** Delivery Atoms. write an Authority Mode override **only** **when** explicitly selected for that unit; an omitted override remains inherited rather than copied as an explicit value. references **and** observations **must** distinguish the declared unit from its existing Carrier **and** Goal coverage.

## Details
