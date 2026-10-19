---
atom_id: CA-R-1959
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Actor/Type: AI Agent"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-18 03:34:02 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1959-CORE_META_MODEL--define-entity-continuant-actor-type-ai-agent.md
  source_atom_id: CA-R-1959
  source_atom_revision: 2
  source_sha256: a8993116607546224887efac541f128add126c94e9161fe7d6b8d1a32e51ef1e
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Entity/Continuant/Actor/Type: AI Agent

## Scope

AI Agents.

## Claim

an AI Agent **means** an Actor that performs delegated work using an AI model.

## Details

Candidate #6 retains AI Agent under Actor and maps its permission limits to Actor/Type: AI Agent.Permissions. CA-R-852 and CA-R-1552 govern those permissions but do not define the Actor kind. This definition grants no additional authority.
