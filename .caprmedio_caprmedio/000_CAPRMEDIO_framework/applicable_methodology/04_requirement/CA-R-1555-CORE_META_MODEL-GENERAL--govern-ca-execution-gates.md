---
subjects:
  governs: "Entity/Continuant/Actor/Type: AI Agent"
  depends_on:
    ["Entity/Continuant/Actor/Type: AI Agent", "Entity/Continuant/Actor/Type: Operator", "AI Agent Delegation", "Confidence Threshold"]
version: 7
updated_at: "2026-10-15 18:44:19 +0000"
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
  source_atom_revision: 7
  source_sha256: 4b5f3cd834932e43d7c2fa25b8afd5b25723c0e245241a5ee9a1d797fdfae130
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
