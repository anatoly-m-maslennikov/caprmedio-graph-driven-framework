---
atom_id: CA-R-2151
ref_id: CA-R-2151
container:
  scope_unit: CA-SU-14
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication <+ Interface Contracts
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction
tier: 1
relations:
  child_of:
  - CA-R-2653
status: Active
version: 19
updated_at: 2026-11-11 16:25:55 +0400
subject_scopes:
- scope-topology
semantic_shape: relational
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relational_endpoints:
  controller:
    scope_unit: ./AGENTIC/SKILLS
    content_role: requirement
  followers:
  - scope_unit: ./PROGRAMMATIC/MCP
    content_roles:
    - delivery
author: Anatoly Maslennikov
current_scope_unit: FRAMEWORK_ENGINE
carrier_destination:
  file:
    name: CA-R-2151-FRAMEWORK_ENGINE-RULE--supply-the-mcp-tool-interface-to-skills.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement
---

## Summary

Supply the MCP Tool interface to SKILLS

## Claim

### Prose Claim

MCP supplies SKILLS with the current generated discovery and invocation interface for active Tools. SKILLS select and use it without redefining Tool behavior. MCP preserves each Tool's identity, accepted inputs, structured outputs and failure meaning.
