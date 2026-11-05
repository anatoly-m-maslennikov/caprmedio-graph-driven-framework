---
atom_id: CA-R-1096
ref_id: CA-R-1096
container:
  scope_unit: CA-SU-15
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
tier: 3
status: Active
version: 19
updated_at: 2026-11-02 19:44:26 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
---
# Summary

Supply active TOOLS to MCP

## Scope

PROGRAMMATIC behavior governing MCP.

## Claim

MCP **must** project one callable frontier for active declared CAPRMEDIO Tools and declared Workflows, validate their machine-invocation contracts, omit inactive or disabled declarations, report invalid declared capability explicitly, and delegate unchanged. Internal CONNECTORS/adapters and PROJECT_TOOLS are not callable frontier members. Direct read or query calls do not require a Workflow Orchestrator wrapper.

## Details
