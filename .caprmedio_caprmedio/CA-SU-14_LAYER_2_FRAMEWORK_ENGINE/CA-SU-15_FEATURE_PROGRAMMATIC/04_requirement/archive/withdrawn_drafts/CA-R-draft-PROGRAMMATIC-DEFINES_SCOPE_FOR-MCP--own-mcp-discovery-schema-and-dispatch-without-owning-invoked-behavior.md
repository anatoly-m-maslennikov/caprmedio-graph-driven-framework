---
atom_id: CA-R-draft
content_role: Requirement
type: Scope Definition
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit.Scope
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations: {}
tier: 3
---
## Summary

Own MCP discovery, schema and dispatch without owning invoked behavior

## Claim scope

MCP.

## Claim

MCP **must** own the provider-neutral Model Context Protocol discovery, schema, **and** dispatch interface through which an agent invokes active CAPRMEDIO Tools, receives ACTION_PROMPTS **or** OPERATOR_PROMPTS, **and** starts **or** resumes Workflows. MCP **must not** own Tool behavior, Prompt content, Workflow coordination, Skill procedures, application behavior, **or** agent-host-specific packaging.
