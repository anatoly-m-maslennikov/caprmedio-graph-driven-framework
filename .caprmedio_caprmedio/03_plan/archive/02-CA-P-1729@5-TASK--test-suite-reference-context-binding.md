---
atom_id: CA-P-1729@5
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
updated_at: 2026-10-24 11:29:41 +0400
subjects:
  governs: Subject/Engineering/Release Testing/Executor Admission
  depends_on:
  - Subject/Engineering/Implementation
  - Subject/Engineering/Implementation Evaluation
  - Manifest
  - Subject/Engineering/Release Testing/Executor Admission
relations:
  is_decomposition_of:
  - CA-P-1727
tier: 3
---
# Summary

Test suite reference-context binding

## Objective

Create mock and golden tests for exact current control closure and its capture/publication freshness proof.

## Details

Test missing, injected, unsafe, symlinked, stale-before-execution and changed-during-execution control rows; require the actual consumed references, not a matching digest alone. Expected bounded effort <=15 minutes.

## Definition of Done

The owned work is independently accepted and its real verification result is saved. Source or mock proof alone does not close the actual Release gate.

## Results

Twelve reference-context tests pass, including every admitted root and a transitive pin mutated in both pre-/post-execution rederivation cases, descriptor-byte/mode races, path/closure refusals and unchanged shared reader globals. Two separate Suite Owner timing tests prove before-executor refusal and after-executor stale evidence. Saved in 689dd212f.
