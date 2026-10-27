---
atom_id: CA-P-1766@5
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
updated_at: 2026-10-24 08:22:45 +0400
subjects:
  governs: Isolate suite child temporaries and imports
  depends_on:
  - Implementation
  - Subject/Engineering/Evaluation
  - Subject/Engineering/Workflow
  - Subject/Engineering/Action
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  is_decomposition_of:
  - CA-P-1755
  blocks: []
tier: 3
---
# Summary

Isolate suite child temporaries and imports

## Objective

Isolate suite child temporaries and imports under the parent's exact source contract.

## Details

suite_driver_repair exclusively owns RELEASE_VERSION/run_release_suite.py and tests/test_run_release_suite.py.

Estimated execution slice <=15 minutes. Preserve other workers' changes. Root alone owns index, commits and actual shared runtime effects. Tests and disposable smoke evidence are not release promotion.

## Definition of Done

Fixed child scratch and same-name flat-module import regressions pass without candidate-byte changes.

## Pre-execution review

Root accepts this exclusive bounded assignment as the minimal current parent repair. Preserve installed N and truthful observed effects.

## Recorded verification

8b8d74bb5; sixteen driver tests passed, including fixed scratch and same-name local import isolation. Root's combined executor/driver command passed 27 cases.
