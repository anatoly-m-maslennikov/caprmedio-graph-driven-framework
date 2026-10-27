---
atom_id: CA-P-2588@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 5
updated_at: 2026-10-24 10:35:14 +0400
subjects:
  governs: Subject/Engineering/Workflow Orchestration/Action Realization
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2585
  depends_on:
  - CA-P-2578
  relates_to:
  - CA-P-2577
  - CA-E-539
tier: 3
---
# Summary

Decompose native Action registration by capability

## Objective

Replace the oversized native handler body with cohesive capability-owned adapters and a small composition boundary. Preserve every existing native Action and failure/result contract, including dirty earlier error-boundary work.

## Details

The Operator explicitly refused a source-size exception and selected refactoring legacy files first. Every leaf is at most 15 minutes own work; split before expanding. New or materially changed Python files must meet the applicable <=200 physical-line target and small cohesive unit boundaries; no mixin/namespace class or imported-method facade substitutes for responsibility decomposition. Preserve the pinned C901/format/lint and applicable typing baseline. Use the locked Project virtual environment, disable bytecode writes and keep disposable test state below configured Project Temporary State. Do not revert other workers' changes. One Task per file, exact predecessor history; review/update dependants after each completed Task.

Dependency review: canonical capability extraction depends on reviewed source/test preparation CA-P-2578, not completion of unrelated freeze/dispatch extraction. Creation, replacement, assessed lifecycle update and current-state status leaves are extracted in exclusive worker scopes and reviewed before integration. Corrected mixed-effect selection and exact no-op/terminal mappings are guarded by focused regressions. Keep only canonical owner behavior; remove temporary class-wrapper normalization. Original executor assembly/caller integration remains under one writer.

### Definition of Done

Retain actual before/after focused tests, changed paths, source/unit/complexity measurements and explicit unresolved limits. Preserve frozen test oracle bytes and current public behavior before new shared-context feature work. No production MCP, release, deployment, full suite, source-policy edits or Git publication.

### Refactor gate checkpoint — 22 October 2026

Native capability factories now have one lifecycle dispatch owner, canonical creation/status result mapping and changed-effect filtering. Compiler and query overlays retain their precedence, and registry state is owned by selected_execution_registration. Subject-batch callers use canonical root/I/O/planning capabilities rather than removed private executor helpers. The 23-test executor baseline, seven Subject-batch execution checks, related composition checks and final independent review passed. No current shared-context Action was implemented.
