---
atom_id: CA-P-1814@8
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 8
updated_at: 2026-10-24 20:02:00 +0400
subjects:
  governs: Subject/Engineering/Evaluation Implementation
  depends_on:
  - Subject/Engineering/Implementation
  - Subject/Engineering/Evaluation Implementation
  - Subject/Engineering/Manifest
  - Subject/Engineering/Workflow
  - Subject/Engineering/Action
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  is_decomposition_of:
  - CA-P-1809
  relates_to:
  - CA-C-514
tier: 3
---
# Summary

Repair sealed MCP startup and query fixtures

## Objective

repair the MCP fixtures to use the declared sealed source context and retain bounded startup diagnostics.

## Details

test_rmed_workflow_mcp.py; demonstrate protocol, gather/check/fix and registered query discovery in a source-equivalent sealed fixture.

## Definition of Done

the confirmed defect is explained and repaired against current authority; source-equivalent focused regressions have a captured terminal result and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.

## Acceptance evidence

independent review accepts canonical selected-manifest/query-source fixture construction and bounded startup stderr. after final frozen D580 v7/D572 v16 publication, the designated host-tests interpreter completed all four MCP fixture tests in 12.935 seconds, exit 0. no legacy live-tree authority fallback or weakened query coverage was introduced.

this is bounded fixture acceptance only; actual complete Release acceptance remains with CA-P-1809 and CA-P-1117.
