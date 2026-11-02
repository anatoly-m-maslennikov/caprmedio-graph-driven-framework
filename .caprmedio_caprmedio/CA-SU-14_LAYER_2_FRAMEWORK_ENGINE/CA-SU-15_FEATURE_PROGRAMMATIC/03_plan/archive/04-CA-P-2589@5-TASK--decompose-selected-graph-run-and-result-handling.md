---
atom_id: CA-P-2589@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 5
updated_at: 2026-10-24 10:35:14 +0400
subjects:
  governs: Subject/Engineering/Workflow Orchestration/Run Execution Dispatch
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2585
  depends_on:
  - CA-P-2586
  relates_to:
  - CA-P-2577
  - CA-E-539
tier: 3
---
# Summary

Decompose selected graph Run and result handling

## Objective

Split graph execution into explicit bounded state/transition/effect recording responsibilities while preserving retry counts, actual effects, interruption/cancellation, retained results and duplicate-effect refusal.

## Details

The Operator explicitly refused a source-size exception and selected refactoring legacy files first. Every leaf is at most 15 minutes own work; split before expanding. New or materially changed Python files must meet the applicable <=200 physical-line target and small cohesive unit boundaries; no mixin/namespace class or imported-method facade substitutes for responsibility decomposition. Preserve the pinned C901/format/lint and applicable typing baseline. Use the locked Project virtual environment, disable bytecode writes and keep disposable test state below configured Project Temporary State. Do not revert other workers' changes. One Task per file, exact predecessor history; review/update dependants after each completed Task.

Dependency review: source graph inputs and contracts are reviewed; graph traversal extraction is independently ready while native handler integration proceeds. Extract Action context, one-Action execution and graph terminal traversal with explicit root/handlers/session/frozen inputs, preserving all legacy IDs, context, retries, visit limits, source edges, actual receipts, partial outcomes and no-replay recovery. No untyped self proxy, new registry or current Integrated feature is permitted.

### Completion evidence — 22 October 2026

Five canonical graph modules separate context construction, one-Action execution, traversal, graph completion and terminal recording. All meet the formatted <=200 physical-line bound; the largest recursive executable statement count is 39, with cohesive 26–40 units reviewed explicitly. Strict Mypy, pinned Ruff format/lint/C901, four durable parity tests and six related focused legacy checks passed. Frozen corpus data was not rewritten.

Independent review closed CA-C-577 after repairing restored-Action membership timing, exact writer/terminal diagnostics, typed prior-result retention and unconditional final graph-projection writes after both terminal attempts. The retained tests cover recovery membership, O016 revisit order/IDs and unconfirmed projection receipt write ordering. Final public-class/caller integration and its complete related acceptance remain CA-P-2590; this leaf does not accept CA-P-2595 or admit current shared-context features.

### Definition of Done

Retain actual before/after focused tests, changed paths, source/unit/complexity measurements and explicit unresolved limits. Preserve frozen test oracle bytes and current public behavior before new shared-context feature work. No production MCP, release, deployment, full suite, source-policy edits or Git publication.
