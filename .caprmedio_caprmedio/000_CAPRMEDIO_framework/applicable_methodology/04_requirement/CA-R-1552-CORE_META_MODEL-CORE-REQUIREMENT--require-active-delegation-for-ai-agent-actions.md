---
subjects:
  governs: "Entity/Continuant/Actor/Type: AI Agent"
  depends_on:
    ["Entity/Continuant/Actor/Type: AI Agent", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Actor/Type: AI Agent.Permissions"]
version: 7
updated_at: "2026-10-16 12:08:31 +0000"
relations:
  child_of:
    - CA-P-034
atom_id: "CA-R-1552"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1552-CORE_META_MODEL-CORE-REQUIREMENT--require-active-delegation-for-ai-agent-actions.md
  source_atom_id: CA-R-1552
  source_atom_revision: 7
  source_sha256: be778c629e3f1edc99f440a97b73cf3abc7d4c4367251381dd6c315ff8fa1a92
  original_relations_sha256: b47bf49353063d138eaaafb2507e53893b8f65ed84f88d6c603da43b611c30d9
---
# Summary

Require active delegation for AI Agent actions

## Scope

AI Agent actions under active Operator-issued delegation.

## Claim

an AI Agent **may** perform **or** authorize a governed action **without** per-action Operator approval **only** **when** an active Operator-issued delegation authorizes that identified Agent, action, target scope, **and** applicable constraints.

## Details
