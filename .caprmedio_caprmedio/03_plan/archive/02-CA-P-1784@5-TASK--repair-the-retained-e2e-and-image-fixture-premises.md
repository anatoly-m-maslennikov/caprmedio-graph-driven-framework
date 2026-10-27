---
atom_id: CA-P-1784@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 5
updated_at: 2026-10-24 08:16:43 +0400
subjects:
  governs: retained E2E Docker identity fixture and image acceptance premises
  depends_on:
  - Implementation
  - Subject/Engineering/Evaluation Implementation
  - Source Carrier
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  is_decomposition_of:
  - CA-P-1782
  relates_to:
  - CA-C-498
tier: 3
---
# Summary

Repair the retained e2e and image fixture premises

## Objective

repair retained E2E Docker identity fixture and image acceptance premises without relaxing the accepted release or source-currentness boundaries.

## Details

- this bounded lane feeds a fresh source-bound N10; retain failed N9 without replay.
- root owns Git, integration, source pins, canonical refresh and actual dispatch. workers preserve other lanes' changes.
- local fixture/source acceptance is not full Release acceptance; installed N remains unchanged.

## Definition of Done

the two-file fixture delta is independently accepted and committed at 50ef09c37. retained-E2E tests pass 2/2; the full mocked image Unit module passes 53/53 in 862.154 seconds. only host executable discovery is mocked, while exact N/package/Skill/source/JUnit/currentness validation and negative tampering cases remain real. the disposable fixture reuses the exact D580 control closure, without folder discovery or a public runtime change. this is local fixture proof, not actual candidate image or Docker E2E acceptance.
