---
atom_id: CA-R-2782
ref_id: CA-R-2782
container:
  scope_unit: CA-SU-43
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
status: Active
version: 2
updated_at: 2026-11-05 06:00:43 +0400
carrier_destination:
  file:
    name: CA-R-2782-WORKBENCH-RULE--workbench-can-restart-without-restarting-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Workbench can restart without restarting MCP

## Claim

Allow the Operator or an AI Agent to restart the selected Project's Workbench through MCP or a health-page button without restarting MCP, other services or the container. Restart closes the old Workbench owner, rebuilds its index from the admitted Current/Draft Atom sources and Current Scope Unit Declarations, and clears temporary query results. It preserves source files and saved queries and Worksheets. Return success only after the replacement Workbench is ready. If sources or startup remain invalid, return an explicit failure and leave Workbench unavailable until another explicit restart. Do not retry automatically.

## Details

An invalid Scope Unit Declaration continues to stop indexing and require explicit restart. Fixing its file alone does not restart Workbench. The service operation is synchronous and does not create a Workflow, queue, background restart job or Business Journal event.

Opening the health page does not restart anything. Restart requires an explicit button action, and its result is visible on that page. The health button and MCP expose the same operation and preserve the same data.
