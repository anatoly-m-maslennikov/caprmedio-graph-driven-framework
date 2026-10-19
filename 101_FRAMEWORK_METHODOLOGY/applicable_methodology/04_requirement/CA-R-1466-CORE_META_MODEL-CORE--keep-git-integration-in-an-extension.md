---
subjects:
  governs: "Extension"
  depends_on:
    ["Core Meta-Model", "Entity/Continuant/History/Journal", "Entity/Continuant/Projection", "Project Configuration"]
version: 6
updated_at: "2026-10-15 18:43:24 +0000"
relations: {}
atom_id: "CA-R-1466"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1466-CORE_META_MODEL-CORE--keep-git-integration-in-an-extension.md
  source_atom_id: CA-R-1466
  source_atom_revision: 6
  source_sha256: 8da64aa7951dbc57addd560919341f1e9bf6ee83ad30214d07ff3b81f3be40fa
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Git integration in an Extension

## Scope

Git integration in the Core Meta-Model.

## Claim

Git integration **must** be optional Extension authority, **not** a prerequisite of the Core Meta-Model. Git commit policies, commit-message encodings, hooks, **and** event-to-commit references belong **to** that Extension; selecting it **must not** replace the authoritative Journal **or** make Git history an independent source for the same recorded facts. the Core Meta-Model **must** remain applicable **without** Git integration.

## Details
