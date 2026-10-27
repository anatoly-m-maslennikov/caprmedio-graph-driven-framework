---
atom_id: CA-P-1751
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 10
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Evaluation Implementation
  depends_on:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Implementation Evaluation
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Engineering/Image
  - Subject/Graph Node/Engineering/Release Testing/Executor Admission
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  is_decomposition_of:
  - CA-P-1744
  blocks: []
tier: 3
---
# Summary

Exercise candidate E2E boundaries with golden inputs

## Objective

Use the presealed fixture to test receipt tamper/removal/cross-candidate binding, exact phase-map membership, no-skip/nonzero testcase JUnit, configured limits, source drift, closed context and immutable image propagation. Test doubles remain non-passing actual Release evidence.

## Details

Ownership: RELEASE_VERSION/test_release_e2e_gate.py, test_release_e2e_context.py and test_run_release_e2e.py. Expected execution slice <=15 minutes. Workers share the checkout and preserve edits outside their exclusive scope. Root owns integration and Git. Source/currentness, permission and missing evidence guards remain intact.

## Definition of Done

Focused behavior tests exercise every specified branch with explicit expected outcomes. Missing fixture or failed cases remain unfinished; no Docker pass is claimed.

## Pre-execution review

Root selects this bounded decomposition to finish the accepted R1890/M346/E589/D582 contract, not a narrower smoke-test substitute. Existing retained N, public routes, pending Runs and canonical Journal history remain protected.

## Recorded verification

Local implementation acceptance is saved in 7874fc864 and 5e0dfee93. The complete private gate module passed 11/11 tests after bounded failed/malformed/empty JUnit retention was fixed; the affected method also passed independently. Narrow D582#10 review accepted the final branch. Earlier context/Driver/phase-map, Runtime image-binding and actual stdio transport results remain retained. Synthetic image/command observations are mock data, not Docker or Release proof. No full-suite, installation, promotion or retirement result is claimed.
