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
  governs: "Entity/Node/Continuant/Actor/Type: AI Agent"
relations:
  child_of:
  - CA-R-1174
version: 3
updated_at: "2026-10-19 15:54:10 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1959-CORE_META_MODEL--define-entity-continuant-actor-type-ai-agent.md
  source_atom_id: CA-R-1959
  source_atom_revision: 3
  source_sha256: c7b0ebcf46452fa7fd5bf4586729a7ae3749512c800f2842ed7db0301de03425
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
