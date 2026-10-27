---
atom_id: CA-P-1805@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 4
updated_at: 2026-10-24 08:47:53 +0400
subjects:
  governs: Repair N12 selected Run fixtures
  depends_on:
  - Subject/Engineering/Implementation
  - Subject/Engineering/Evaluation Implementation
  - Source Carrier
relations:
  is_decomposition_of:
  - CA-P-1801
  relates_to:
  - CA-C-510
tier: 3
---
# Summary

Repair N12 selected Run fixtures

## Objective

repair confirmed selected-run/MCP fixture or code mismatches while preserving existing authority, source freshness and recording contracts.

## Details

- this lane owns 4 failing cases from the frozen N12 Unit report, not a new scope expansion.
- use disposable fixtures; preserve actual Run, runtime, Journal and source snapshot evidence.
- coordinate shared production dependencies instead of overlapping another worker. root integrates accepted changes and current pins.

## Definition of Done

the observed failures are explained and fixed against current authority; focused regression suites pass and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.

## Result

the selected-execution suite passes 20 tests and the isolated MCP suite passes 4 tests. the fixtures copy exact bound sources into disposable Projects, allow bounded gateway cold start and correctly stop before a next Step while terminal recording is pending. independent review accepts the changes; actual all-route release proof remains separate.
