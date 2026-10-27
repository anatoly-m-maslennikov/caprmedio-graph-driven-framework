---
atom_id: CA-P-1791@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 6
updated_at: 2026-10-24 19:58:06 +0400
subjects:
  governs: runner TMPDIR fixtures and explicit historical Actor bytes
  depends_on:
  - Subject/Engineering/Implementation
  - Subject/Engineering/Evaluation Implementation
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  is_decomposition_of:
  - CA-P-1782
  relates_to:
  - CA-C-498
tier: 3
---
# Summary

Repair the stdio scratch and legacy evidence fixtures

## Objective

repair runner TMPDIR fixtures and explicit historical Actor bytes without relaxing the accepted release or source-currentness boundaries.

## Details

- this bounded lane feeds a fresh source-bound N10; retain failed N9 without replay.
- root owns Git, integration, source pins, canonical refresh and actual dispatch. workers preserve other lanes' changes.
- local fixture/source acceptance is not full Release acceptance; installed N remains unchanged.

## Definition of Done

7aee87a46; four MCP and eighteen declared-Subject cases pass; no production changes.
