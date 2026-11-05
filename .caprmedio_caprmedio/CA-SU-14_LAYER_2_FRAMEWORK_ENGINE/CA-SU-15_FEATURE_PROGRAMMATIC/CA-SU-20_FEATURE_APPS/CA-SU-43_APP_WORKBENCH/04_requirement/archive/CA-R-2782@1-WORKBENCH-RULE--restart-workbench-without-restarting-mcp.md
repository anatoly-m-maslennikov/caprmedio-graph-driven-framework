---
atom_id: CA-R-2782
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 1
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
updated_at: 2026-11-05 05:49:16 +0400
carrier_destination:
  file:
    name: CA-R-2782@1-WORKBENCH-RULE--restart-workbench-without-restarting-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
---

## Summary

Workbench can restart without restarting MCP

## Claim

Allow the Operator or an AI Agent to restart the selected Project's Workbench through MCP without restarting MCP, other services or the container. Restart closes the old Workbench owner, rebuilds its index from the admitted Current/Draft Atom sources and Current Scope Unit Declarations, and clears temporary query results. It preserves source files and saved queries and Worksheets. Return success only after the replacement Workbench is ready. If sources or startup remain invalid, return an explicit failure and leave Workbench unavailable until another explicit restart. Do not retry automatically.

## Details

An invalid Scope Unit Declaration continues to stop indexing and require explicit restart. Fixing its file alone does not restart Workbench. The service operation is synchronous and does not create a Workflow, queue, background restart job or Business Journal event.
