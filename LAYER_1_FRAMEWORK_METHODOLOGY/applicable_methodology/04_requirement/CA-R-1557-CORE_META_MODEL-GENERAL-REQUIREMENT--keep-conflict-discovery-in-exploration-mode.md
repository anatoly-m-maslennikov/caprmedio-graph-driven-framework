---
subjects:
  governs: "Entity/Node/Continuant/Actor/Type: AI Agent"
  depends_on:
    ["Entity/Node/Continuant/Actor/Type: AI Agent", "Entity/Node/Continuant/Actor/Type: Operator", "Exploration Mode", "Entity/Node/Continuant/Atom/Content Role: Concern"]
version: 8
updated_at: "2026-10-19 15:53:28 +0400"
relations: {"child_of":["CA-R-1702"]}
atom_id: "CA-R-1557"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1557-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-conflict-discovery-in-exploration-mode.md
  source_atom_id: CA-R-1557
  source_atom_revision: 8
  source_sha256: 497f1502e8b3e6ad7be66aa2e28baa93659db48411071e22b054390b6fd56b48
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep conflict discovery in Exploration Mode

## Scope

AI Agent discovery of conflicts in Exploration Mode.

## Claim

an AI Agent **must** keep a discovered conflict **in** Exploration Mode; it **may** create a Concern for that conflict **only** **when** the Operator requests persistence **or** defers its resolution.

## Details
