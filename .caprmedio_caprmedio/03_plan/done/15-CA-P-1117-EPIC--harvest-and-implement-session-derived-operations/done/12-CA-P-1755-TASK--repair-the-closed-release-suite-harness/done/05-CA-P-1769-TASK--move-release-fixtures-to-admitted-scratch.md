---
atom_id: CA-P-1769
ref_id: CA-P-1769
role: Plan
form: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 10
updated_at: 2026-11-02 19:44:26 +0400
topics:
  main_subject: Subject/Graph Node/Engineering/Evaluation Implementation
  dependencies:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Evaluation Implementation
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  is_decomposition_of:
  - CA-P-1755
tier: 3
container:
  atom: CA-P-1755
carrier_destination:
  file:
    name: 5-CA-P-1769-TASK--move-release-fixtures-to-admitted-scratch.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/done/12-CA-P-1755-TASK--repair-the-closed-release-suite-harness/done
---
# Summary

Move release fixtures to admitted scratch

## Objective

Move release fixtures to admitted scratch under the parent's exact source contract.

## Details

suite_scratch_executor exclusively owns tests/test_bootstrap_image.py, test_release_e2e_retained.py, test_release_e2e_gate.py and test_release_full_gate.py.

Estimated execution slice <=15 minutes. Preserve other workers' changes. Root alone owns index, commits and actual shared runtime effects. Tests and disposable smoke evidence are not release promotion.

## Definition of Done

The four complete fixture modules pass under the fixed Project scratch convention; no extra mounts or exclusions are added.

## Pre-execution review

Root accepts this exclusive bounded assignment as the minimal current parent repair. Preserve installed N and truthful observed effects.

## Recorded verification

8b8d74bb5; all 32 assigned fixture cases passed (12 bootstrap, 2 retained E2E, 11 E2E gate, 7 Full Gate). No extra source-write mounts were added.
