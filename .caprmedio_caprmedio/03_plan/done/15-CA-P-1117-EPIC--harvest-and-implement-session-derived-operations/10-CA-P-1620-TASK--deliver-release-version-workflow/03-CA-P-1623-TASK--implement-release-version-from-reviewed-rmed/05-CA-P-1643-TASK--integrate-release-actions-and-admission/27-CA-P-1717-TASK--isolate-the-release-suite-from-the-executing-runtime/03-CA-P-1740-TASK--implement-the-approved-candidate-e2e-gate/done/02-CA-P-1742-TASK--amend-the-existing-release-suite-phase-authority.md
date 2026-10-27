---
atom_id: CA-P-1742
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 9
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Release
  depends_on:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Evaluation
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Engineering/Image
  - Subject/Graph Node/Engineering/Release Testing/Executor Admission
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  is_decomposition_of:
  - CA-P-1740
  blocks:
  - CA-P-1747
  - CA-P-1748
tier: 3
---
# Summary

Amend the existing Release suite phase authority

## Objective

Separate the closed Unit Gate and final complete gate in the existing Suite and image-build authority.

## Details

Own R1886/M343/E586/D579/D564 and full predecessor archives. Preserve the complete module inventory, source/current-control proofs and candidate identity. Unit evidence gates image construction; Unit plus E2E evidence gates promotion. ETA <=15 minutes.

## Definition of Done

The owned source or implementation is independently accepted and actual scoped verification is saved. Mock or source acceptance does not close live Docker, complete-suite, installation or promotion gates.

## Pre-execution review

Root accepts this bounded decomposition of the Operator-approved host E2E design. Respect the stated dependency and file-ownership boundaries. The existing isolated Unit executor, current public manifest, pending Runs and retained N remain protected.

## Result

Independent review accepted R1886@2/M343@3/E586@2/D579@4/D564@2: exact Unit/E2E partition, Unit-before-image and aggregate-before-promotion; schema-2 controls and source probes remain authoritative. Full predecessor bytes were verified against HEAD.

Saved source: 7d14bebd9. This is source acceptance only; actual E2E, complete-suite and Release gates remain open.
