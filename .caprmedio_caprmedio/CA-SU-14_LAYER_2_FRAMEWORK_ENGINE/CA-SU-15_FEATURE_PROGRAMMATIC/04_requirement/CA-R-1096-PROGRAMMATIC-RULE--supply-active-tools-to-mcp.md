---
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
version: 19
updated_at: 2026-11-02 19:44:26 +0400
atom_id: CA-R-1096
ref_id: CA-R-1096
role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
tier: 3
form: Rule
container:
  scope_unit: CA-SU-15
---
# Summary

Supply active TOOLS to MCP

## Scope

PROGRAMMATIC behavior governing MCP.

## Claim

MCP **must** project one callable frontier for active declared CAPRMEDIO Tools and declared Workflows, validate their machine-invocation contracts, omit inactive or disabled declarations, report invalid declared capability explicitly, and delegate unchanged. Internal CONNECTORS/adapters and PROJECT_TOOLS are not callable frontier members. Direct read or query calls do not require a Workflow Orchestrator wrapper.

## Details
