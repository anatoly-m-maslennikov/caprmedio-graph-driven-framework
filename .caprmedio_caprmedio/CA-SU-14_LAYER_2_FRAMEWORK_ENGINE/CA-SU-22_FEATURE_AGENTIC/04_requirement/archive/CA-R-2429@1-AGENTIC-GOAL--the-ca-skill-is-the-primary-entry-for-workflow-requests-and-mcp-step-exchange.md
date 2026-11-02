---
atom_id: CA-R-2429@1
content_role: Requirement
current_scope_unit: AGENTIC
claim_target_scope_unit: SKILLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Entry
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
version: 1
updated_at: 2026-10-29 23:57:07 +0400
relations: {}
tier: 3
type: Goal
---
## Summary

The ca Skill is the primary entry for Workflow requests and MCP Step exchange

## Claim scope

requests submitted by Operators and AI Agents through the CAPRMEDIO Main Skill `ca` for methodology-defined Workflow execution and MCP Step instructions and results.

## Claim

FRAMEWORK_ENGINE **must** provide `ca` as the primary Skill entry point through which Operators **and** AI Agents:

- submit requests **to** methodology-defined Workflow execution; **and**
- exchange current Step instructions **and** results through MCP.
