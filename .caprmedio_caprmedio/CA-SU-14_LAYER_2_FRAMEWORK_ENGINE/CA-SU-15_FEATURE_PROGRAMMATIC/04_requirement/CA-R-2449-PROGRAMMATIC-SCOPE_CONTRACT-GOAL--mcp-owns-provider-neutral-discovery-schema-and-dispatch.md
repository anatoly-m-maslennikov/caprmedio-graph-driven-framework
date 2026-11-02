---
atom_id: CA-R-2449
content_role: Requirement
type: Goal
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
version: 1
updated_at: 2026-10-30 03:11:57 +0400
relations: {}
tier: 0
---
## Summary

MCP owns provider-neutral discovery, schema and dispatch

## Claim scope

MCP.

## Claim

MCP **must** own the provider-neutral Model Context Protocol discovery, schema, **and** dispatch interface through which an agent:

- invokes active CAPRMEDIO Tools;
- receives ACTION_PROMPTS **or** OPERATOR_PROMPTS; **and**
- starts **or** resumes Workflows.

MCP **must not** own **any** of the following:

- Tool behavior;
- Prompt content;
- Workflow coordination;
- Skill procedures;
- application behavior; **or**
- agent-host-specific packaging.
