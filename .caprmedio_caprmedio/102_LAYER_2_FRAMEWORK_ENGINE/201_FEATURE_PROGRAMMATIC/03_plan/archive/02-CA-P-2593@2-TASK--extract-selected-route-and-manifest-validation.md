---
atom_id: CA-P-2593@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
version: 2
updated_at: '2026-10-22T10:22:32Z'
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2591
  depends_on:
  - CA-P-2592
  relates_to:
  - CA-P-2577
  - CA-E-539
---
# Summary

Extract selected route and manifest validation

## Objective

Separate route/manifest/source-admission validation and effect-free route adapter behavior, keeping one canonical owner per rule and preserving the frozen route corpus. Verify the <=200-file/small-unit bounds and focused baseline.

## Details

The Operator explicitly refused a source-size exception and selected refactoring legacy files first. Every leaf is at most 15 minutes own work; split before expanding. New or materially changed Python files must meet the applicable <=200 physical-line target and small cohesive unit boundaries; no mixin/namespace class or imported-method facade substitutes for responsibility decomposition. Preserve the pinned C901/format/lint and applicable typing baseline. Use the locked Project virtual environment, disable bytecode writes and keep disposable test state below configured Project Temporary State. Do not revert other workers' changes. One Task per file, exact predecessor history; review/update dependants after each completed Task.

Accepted route/manifest decomposition after reviewed request/pin results. The worker reports before/after selected-route baseline21, new diagnostics1, definition/pin17, focused discovery/selection/error/release31 and simple-release11 all passing; real Ruff format/lint/C901 and strict Mypy15 pass. Independent re-review confirms one canonical error/definition owner, exact diagnostics, unchanged route policy and JSON packaging closure. Root measured all15 files below200 physical lines, maximum logical function36; seven26–40-line units each retain one cohesive validation, registration, adapter or release job. Unrelated executor compatibility failures remain outside this route acceptance.

### Definition of Done

Retain actual before/after focused tests, changed paths, source/unit/complexity measurements and explicit unresolved limits. Preserve frozen test oracle bytes and current public behavior before new shared-context feature work. No production MCP, release, deployment, full suite, source-policy edits or Git publication.
