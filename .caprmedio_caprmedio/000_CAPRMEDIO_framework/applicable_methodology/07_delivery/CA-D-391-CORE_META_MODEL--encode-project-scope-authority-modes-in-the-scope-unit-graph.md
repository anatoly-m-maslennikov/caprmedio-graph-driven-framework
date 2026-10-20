---
subjects:
  governs: "Project Scope Unit Graph Projection"
  depends_on:
    ["Entity/Node/Continuant/Project.Structure", "Entity/Node/Continuant/Project.Framework Settings", "Authority Mode"]
version: 11
updated_at: "2026-10-19 15:55:42 +0400"
relations:
  child_of:
    - "CA-R-1430"
atom_id: "CA-D-391"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-391-CORE_META_MODEL--encode-project-scope-authority-modes-in-the-scope-unit-graph.md
  source_atom_id: CA-D-391
  source_atom_revision: 11
  source_sha256: fdb70dbbbfb0308dc61ec5081ab3fc866cb6f0fcd4f34200af8b3d2f5446ad89
  original_relations_sha256: 1be50eaa42168c84ffd69ce5d3a59f12850826b66f6c14e32382932fd9c81147
---
# Summary

Encode project scope authority modes in the Scope Unit Graph

## Scope

the `authority_mode` of a retained Project Scope Unit Graph Projection.

## Claim

**if** a Project Scope Unit Graph Projection is retained for compatibility, its `authority_mode` **must** be a derived effective value: an explicit unit override from Project Structure, **otherwise** the applicable Framework Instance Settings selection. it **must not** select **or** own that mode, become a required input **to** a direct Project Structure consumer, **or** require creation of a separate structural Projection.

## Details
