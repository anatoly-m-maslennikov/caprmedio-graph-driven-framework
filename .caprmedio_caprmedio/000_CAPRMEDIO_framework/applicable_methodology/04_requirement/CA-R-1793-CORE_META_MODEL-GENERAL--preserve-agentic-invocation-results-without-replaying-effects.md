---
subjects:
  governs: "Entity/Occurrent/Execution/Step Run"
  depends_on:
    ["Entity/Occurrent/Execution/Step Run", "Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action/Execution Kind", "Entity/Occurrent/Execution/Step Run.Execution Context", "Entity/Continuant/Node/Actor/Type: Operator", "Entity/Continuant/Node/History/Journal"]
version: 4
updated_at: "2026-10-18 03:34:00 +0400"
relations: {"relates_to": ["CA-R-1519", "CA-R-1520", "CA-R-1525", "CA-R-1527"]}
atom_id: "CA-R-1793"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1793-CORE_META_MODEL-GENERAL--preserve-agentic-invocation-results-without-replaying-effects.md
  source_atom_id: CA-R-1793
  source_atom_revision: 4
  source_sha256: aa39d5f442453cd6a4f7066a52ea8d20b692083b459fe77588d4b49c8450a5ae
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Preserve Agentic Invocation results **without** replaying effects

## Scope

repeated delivery **or** reconnection for an Agentic Step Invocation.

## Claim

the receiving context **must** report actual results against the identified Invocation. redelivery **or** reconnection **must not** imply permission **to** repeat already performed effects.

## Details
