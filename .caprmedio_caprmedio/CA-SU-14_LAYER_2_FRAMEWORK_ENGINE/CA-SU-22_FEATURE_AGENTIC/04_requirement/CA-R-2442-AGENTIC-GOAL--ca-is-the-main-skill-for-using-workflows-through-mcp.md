---
atom_id: CA-R-2442
ref_id: CA-R-2442
container:
  scope_unit: CA-SU-22
role: Requirement
form: Goal
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Entry
  dependencies:
  - MODEL//CAPRMEDIO <+ Actor/AI Agent
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Action
  - MODEL//CAPRMEDIO <+ Actor/Operator
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Communication
  - MODEL//CAPRMEDIO <+ Execution/Step Run
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Workflow
tier: 3
status: Active
version: 2
updated_at: 2026-11-10 20:47:54 +0400
current_scope_unit: AGENTIC
claim_target_scope_unit: SKILLS
author: Anatoly Maslennikov
destination:
  file:
    name: CA-R-2442-AGENTIC-GOAL--ca-is-the-main-skill-for-using-workflows-through-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/04_requirement
---
## Summary

`ca` is the main Skill for using Workflows through MCP

## Claim scope

Requests from Operators and AI Agents through the CAPRMEDIO Main Skill `ca` for methodology-defined Workflow execution and MCP Step instructions and results.

## Claim


### Prose Claim
FRAMEWORK_ENGINE **must** provide `ca` as the primary Skill entry point through which Operators **and** AI Agents:

- request Workflows defined by the methodology; **and**
- exchange current Step instructions **and** results through MCP.
