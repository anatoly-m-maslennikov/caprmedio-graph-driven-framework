---
subjects:
  active: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  passive:
  - Entity/Object/Continuant/History
  - Journal
  - Carrier
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-D-440
atom_id: CA-D-443
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Bind Project Structure revisions **to** source evidence

## Claim scope

Project Structure Revision bindings.

## Claim

a Project Structure Revision binding **must** identify the exact authoritative TOML bytes by SHA-256 Digest **and** the completed change event **in** the canonical Event Log under applicable Journal authority. the binding **must** distinguish the selected pre-change state, resulting state, **and** actual completion **or** failure; missing **or** conflicting event evidence leaves provenance currentness unknown. the TOML Carrier **must not** duplicate Atom Revision fields **or** store its own self-referential digest. a consumer **may** parse **and** validate the selected bytes **without** claiming completed change provenance **when** that provenance is unresolved.
