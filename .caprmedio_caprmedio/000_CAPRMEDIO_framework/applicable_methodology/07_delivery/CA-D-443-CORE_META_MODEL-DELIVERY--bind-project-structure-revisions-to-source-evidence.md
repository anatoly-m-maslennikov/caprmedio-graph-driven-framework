---
subjects:
  governs: "Entity/Continuant/Node/Project.Structure"
  depends_on:
    ["Entity/Continuant/Node/History/Revision", "Entity/Continuant/Node/History/Journal", "Entity/Carrier"]
version: 8
updated_at: "2026-10-18 03:34:48 +0400"
relations:
  child_of:
    - "CA-D-440"
atom_id: "CA-D-443"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-443-CORE_META_MODEL-DELIVERY--bind-project-structure-revisions-to-source-evidence.md
  source_atom_id: CA-D-443
  source_atom_revision: 8
  source_sha256: 21abcf0a346218f51afa761ec8f5c09b3915849d4bd83efdac9c5ec91f1e3eda
  original_relations_sha256: 4ea2c90f06a6f75bf31082400ec9137e19d06cdfa3e8d7bded3331399aa3453a
---
# Summary

Bind Project Structure revisions **to** source evidence

## Scope

Project Structure Revision bindings.

## Claim

a Project Structure Revision binding **must** identify the exact authoritative TOML bytes by SHA-256 Digest **and** the completed change event **in** the canonical Event Log under applicable Journal authority. the binding **must** distinguish the selected pre-change state, resulting state, **and** actual completion **or** failure; missing **or** conflicting event evidence leaves provenance currentness unknown. the TOML Carrier **must not** duplicate Atom Revision fields **or** store its own self-referential digest. a consumer **may** parse **and** validate the selected bytes **without** claiming completed change provenance **when** that provenance is unresolved.

## Details
