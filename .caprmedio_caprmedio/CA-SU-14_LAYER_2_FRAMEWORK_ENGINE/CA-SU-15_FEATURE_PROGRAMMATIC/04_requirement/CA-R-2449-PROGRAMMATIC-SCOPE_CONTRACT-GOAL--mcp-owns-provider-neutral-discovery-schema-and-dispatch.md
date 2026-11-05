---
atom_id: CA-R-2449
ref_id: CA-R-2449
role: Requirement
form: Goal
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
version: 1
updated_at: 2026-10-30 03:11:57 +0400
tier: 0
container:
  scope_unit: CA-SU-15
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
