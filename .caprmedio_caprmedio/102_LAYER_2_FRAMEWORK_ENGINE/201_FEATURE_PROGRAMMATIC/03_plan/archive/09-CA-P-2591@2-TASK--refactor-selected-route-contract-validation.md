---
atom_id: CA-P-2591@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
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
  - CA-P-2577
  depends_on: []
  relates_to:
  - CA-P-2577
  - CA-E-539
---
# Summary

Refactor selected route contract validation

## Objective

Container task; children P2592/P2593 split route/request/source validation without changing admission meaning. The current terminal-label feature remains deferred until behavior-preserving refactor checks pass.

## Details

The Operator explicitly refused a source-size exception and selected refactoring legacy files first. Every leaf is at most 15 minutes own work; split before expanding. New or materially changed Python files must meet the applicable <=200 physical-line target and small cohesive unit boundaries; no mixin/namespace class or imported-method facade substitutes for responsibility decomposition. Preserve the pinned C901/format/lint and applicable typing baseline. Use the locked Project virtual environment, disable bytecode writes and keep disposable test state below configured Project Temporary State. Do not revert other workers' changes. One Task per file, exact predecessor history; review/update dependants after each completed Task.

Both contained Tasks CA-P-2592 and CA-P-2593 are Done after functional, source-size/complexity, strict typing and independent architecture review. selected_routes.py is126 physical lines versus1081 before; all15 source carriers are below200. All36 original definitions remain import-compatible, with one canonical error and exact public diagnostics. No new terminal labels, Workflow bindings, release or production behavior were admitted.

### Definition of Done

Retain actual before/after focused tests, changed paths, source/unit/complexity measurements and explicit unresolved limits. Preserve frozen test oracle bytes and current public behavior before new shared-context feature work. No production MCP, release, deployment, full suite, source-policy edits or Git publication.
