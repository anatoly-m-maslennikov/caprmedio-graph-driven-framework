---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Carrier
version: 17
updated_at: 2026-10-27 19:59:25 +0400
relations:
  child_of:
  - CA-D-440
atom_id: CA-D-443
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Bind Project Structure revisions **to** source evidence

## Scope

Project Structure Revision bindings.

## Claim

a Project Structure Revision binding **must** identify the exact authoritative TOML bytes by SHA-256 Digest **and** the completed change event **in** the canonical Event Log under applicable Journal authority. the binding **must** distinguish the selected pre-change state, resulting state, **and** actual completion **or** failure; missing **or** conflicting event evidence leaves provenance currentness unknown. the TOML Carrier **must not** duplicate Atom Revision fields **or** store its own self-referential digest. a consumer **may** parse **and** validate the selected bytes **without** claiming completed change provenance **when** that provenance is unresolved.

## Details
