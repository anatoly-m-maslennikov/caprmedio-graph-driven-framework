---
atom_id: CA-P-1764
content_role: Plan
type: Plan
label: Task
work_sequence_number: 21
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Implementation
  depends_on:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Engineering/Continuant/Carrier
relations:
  is_decomposition_of:
  - CA-P-1117
  blocks:
  - CA-P-1655
tier: 3
---
# Summary

Allow safe canonical workspace ancestors

## Objective

Accept legitimate absolute workspace ancestor aliases while preserving leaf-symlink and protected-authority overlap rejection.

## Details

restart_recovery_finish exclusively owns IMPLEMENTATION_WORKFLOW/implementation_actions.py and its focused test file. Estimated slice <=10 minutes. Reproduce the macOS /var versus /private/var failure using a platform-independent symlinked ancestor. No runtime dispatch, LLM calls, commits or index changes.

## Definition of Done

The two blocked W09 fixtures and native route proof pass; a leaf-symlink workspace and protected overlap still fail before execution.

## Pre-execution review

Root accepts canonicalizing an admitted absolute workspace, not weakening its authority boundary. Actual Docker/queue proof remains a separate gate.

## Recorded verification

cb4bba3e2 retains canonical ancestor admission and mock transport agreement. Twenty-nine focused W09/native cases pass; leaf-symlink and protected-overlap refusal remain. Actual Docker/MCP queue proof is separate.
