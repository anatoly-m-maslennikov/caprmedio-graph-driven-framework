---
atom_id: CA-P-1765@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 5
updated_at: 2026-10-24 08:22:45 +0400
subjects:
  governs: Provide fixed isolated suite scratch
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

Provide fixed isolated suite scratch

## Objective

Provide fixed isolated suite scratch under the parent's exact source contract.

## Details

suite_scratch_executor exclusively owns RELEASE_VERSION/release_suite_execution.py and tests/test_release_suite_execution.py.

Estimated execution slice <=15 minutes. Preserve other workers' changes. Root alone owns index, commits and actual shared runtime effects. Tests and disposable smoke evidence are not release promotion.

## Definition of Done

Fixed bounded tmpfs regression and actual disposable Docker scratch smoke pass; source bind stays read-only.

## Pre-execution review

Root accepts this exclusive bounded assignment as the minimal current parent repair. Preserve installed N and truthful observed effects.

## Recorded verification

8b8d74bb5; eleven executor tests and actual disposable Docker scratch smoke passed with read-only workspace and ephemeral writable tmpfs.
