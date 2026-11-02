---
subjects:
  active: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  passive:
  - Scope Unit
  - Scope Unit.Name
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Type
  - Scope Unit.Label
  - Scope Unit.Local Order
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Navigational Order Number
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Goal'
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Carrier
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-M-291
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Method
form: Implementation Method
---
## Summary

Author Project Structure **without** competing declarations

## Claim scope

Project Structure declarations.

## Claim

**to** express Project Structure, use one declaration for **every** non-root Scope Unit, reference its parent by the reserved Project-root reference **or** the parent's unique Name, **and** keep structural Local Order distinct from Navigational Order Number. retain an explicit Label independently of Ordered/Unordered Type. retain a readable derived Scope Unit Path **only** with its checked derivation from declared parentage **and** applicable Carrier conventions; do not author or persist Structural Level, and physical nesting **must not** silently replace logical parentage. use concrete Carrier bindings as declared values rather than repeating them **in** Goal, Requirement, **or** Delivery Atoms. write an Authority Mode override **only** **when** explicitly selected for that unit; an omitted override remains inherited rather than copied as an explicit value. references **and** observations **must** distinguish the declared unit from its existing Carrier **and** Goal coverage.
