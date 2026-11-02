---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  depends_on:
  - Entity/Object/Continuant/History
  - Entity/Object/Continuant/History/Journal
  - Entity/Carrier
version: 20
updated_at: 2026-10-29 10:13:51 +0400
relations:
  child_of:
  - CA-D-440
atom_id: CA-D-443@20
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Bind Project Structure revisions **to** source evidence

## Claim scope

Project Structure Revision bindings.

## Claim

a Project Structure Revision binding **must** identify the exact authoritative TOML bytes by SHA-256 Digest **and** the completed change event **in** the canonical Event Log under applicable Journal authority. the binding **must** distinguish the selected pre-change state, resulting state, **and** actual completion **or** failure; missing **or** conflicting event evidence leaves provenance currentness unknown. the TOML Carrier **must not** duplicate Atom Revision fields **or** store its own self-referential digest. a consumer **may** parse **and** validate the selected bytes **without** claiming completed change provenance **when** that provenance is unresolved.
