---
atom_id: CA-P-2586@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 4
updated_at: 2026-10-24 10:35:14 +0400
subjects:
  governs: Subject/Engineering/Implementation Binding
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2585
  depends_on: []
  relates_to:
  - CA-P-2577
  - CA-E-539
tier: 3
---
# Summary

Extract source-bound graph and admission reading

## Objective

Extract cohesive deterministic graph/source binding validation from SelectedExecution using explicit typed inputs; preserve exact existing refusal, source-freshness and public compatibility behavior.

## Details

The Operator explicitly refused a source-size exception and selected refactoring legacy files first. Every leaf is at most 15 minutes own work; split before expanding. New or materially changed Python files must meet the applicable <=200 physical-line target and small cohesive unit boundaries; no mixin/namespace class or imported-method facade substitutes for responsibility decomposition. Preserve the pinned C901/format/lint and applicable typing baseline. Use the locked Project virtual environment, disable bytecode writes and keep disposable test state below configured Project Temporary State. Do not revert other workers' changes. One Task per file, exact predecessor history; review/update dependants after each completed Task.

Accepted four cohesive source/edge/assembly/admission modules with explicit root/parameter inputs: selected_graph_sources, selected_source_graph_edges, selected_graph_validation and selected_graph_admission. Real Ruff formatting/lint/C901 and strict typing pass. Root tokenized measurements put all units at<=25 logical lines except the cohesive manifest-location validation at27 (permitted26–40); files remain<=200. Current source pin/path/security checks, graph shape and terminal semantics are preserved. This accepts extraction only: executor integration and any remaining legacy private test seams must still pass CA-P-2590 before feature admission.

### Definition of Done

Retain actual before/after focused tests, changed paths, source/unit/complexity measurements and explicit unresolved limits. Preserve frozen test oracle bytes and current public behavior before new shared-context feature work. No production MCP, release, deployment, full suite, source-policy edits or Git publication.
