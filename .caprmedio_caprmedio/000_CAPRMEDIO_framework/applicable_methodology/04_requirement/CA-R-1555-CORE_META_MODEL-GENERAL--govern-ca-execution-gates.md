---
subjects:
  governs: "Entity/Node/Continuant/Actor/Type: AI Agent"
  depends_on:
    ["Entity/Node/Continuant/Actor/Type: AI Agent", "Entity/Node/Continuant/Actor/Type: Operator", "AI Agent Delegation", "Confidence Threshold"]
version: 8
updated_at: "2026-10-19 15:53:27 +0400"
relations: {"child_of":["CA-R-1713"]}
atom_id: "CA-R-1555"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1555-CORE_META_MODEL-GENERAL--govern-ca-execution-gates.md
  source_atom_id: CA-R-1555
  source_atom_revision: 8
  source_sha256: b4f5efc5538eaa555f3497eb99b144eeefffa8eb431e15d04d3e434b3d03d70c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Govern CA execution gates

## Scope
identified AI Agents considering clarification omission under applicable configured confidence requirements.

## Claim

an identified AI Agent **may** omit clarification **only** **when** confidence **in** **every** following item meets its applicable configured requirement:

- intent;
- scope;
- route;
- entry criteria.

confidence **must not** create delegated authority **or** bypass per-action Operator approval **when** active authority requires it.

## Details
