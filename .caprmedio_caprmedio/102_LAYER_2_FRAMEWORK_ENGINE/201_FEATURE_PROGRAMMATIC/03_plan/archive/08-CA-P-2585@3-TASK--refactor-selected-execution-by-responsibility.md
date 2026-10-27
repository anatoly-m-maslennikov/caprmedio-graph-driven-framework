---
atom_id: CA-P-2585@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 3
updated_at: 2026-10-24 06:04:43 +0400
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2577
  depends_on: []
  relates_to:
  - CA-P-2577
  - CA-E-539
tier: 3
---
# Summary

Refactor selected execution by responsibility

## Objective

Container task with zero implementation work of its own; child Tasks P2586–P2590 preserve public behavior while reducing the oversized execution owner. No feature logic or size exception is accepted.

## Details

The Operator explicitly refused a source-size exception and selected refactoring legacy files first. Every leaf is at most 15 minutes own work; split before expanding. New or materially changed Python files must meet the applicable <=200 physical-line target and small cohesive unit boundaries; no mixin/namespace class or imported-method facade substitutes for responsibility decomposition. Preserve the pinned C901/format/lint and applicable typing baseline. Use the locked Project virtual environment, disable bytecode writes and keep disposable test state below configured Project Temporary State. Do not revert other workers' changes. One Task per file, exact predecessor history; review/update dependants after each completed Task.

### Definition of Done

Retain actual before/after focused tests, changed paths, source/unit/complexity measurements and explicit unresolved limits. Preserve frozen test oracle bytes and current public behavior before new shared-context feature work. No production MCP, release, deployment, full suite, source-policy edits or Git publication.

### Refactor gate checkpoint — 22 October 2026

All five decomposition children are Done and reviewed. The public executor is a 197-line stateful facade over canonical responsibilities, not a mixin, imported-method namespace or untyped self proxy. Public exports, native precedence, source-bound dispatch, Subject batches and no-replay recovery are preserved. CA-P-2590 retains exact focused/static acceptance evidence; CA-P-2595 owns the final refactor-first gate. The matching container hierarchy moves with this Done Plan after its children are Done.
