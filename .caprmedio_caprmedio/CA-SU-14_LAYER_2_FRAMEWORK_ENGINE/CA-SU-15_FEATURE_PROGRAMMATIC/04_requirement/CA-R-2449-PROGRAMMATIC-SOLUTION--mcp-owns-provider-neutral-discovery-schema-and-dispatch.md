---
identity:
  atom_id: CA-R-2449
  ref_id: CA-R-2449
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Solution
  topics:
    main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication"
    dependencies:
    - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication"
  tier: 0
state:
  status: Active
  version: 2
  updated_at: 2026-11-09 00:09:26 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
destination:
  file:
    name: CA-R-2449-PROGRAMMATIC-SOLUTION--mcp-owns-provider-neutral-discovery-schema-and-dispatch.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
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
