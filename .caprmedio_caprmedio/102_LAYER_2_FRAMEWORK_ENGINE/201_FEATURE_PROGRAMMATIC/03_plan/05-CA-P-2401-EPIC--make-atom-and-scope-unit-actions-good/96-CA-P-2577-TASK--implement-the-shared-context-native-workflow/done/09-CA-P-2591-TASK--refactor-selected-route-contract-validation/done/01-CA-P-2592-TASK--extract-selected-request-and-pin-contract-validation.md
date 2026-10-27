---
atom_id: CA-P-2592
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
version: 5
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/MCP.selected Workflow route contract
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2591
  depends_on: []
  relates_to:
  - CA-P-2577
  - CA-E-539
tier: 3
---
# Summary

Extract selected request and pin contract validation

## Objective

Separate request/pin validation and canonical serialization into cohesive bounded modules, preserving closed schemas, exact digest/error behavior, source guards and all declared public/private compatibility imports.

## Details

The Operator explicitly refused a source-size exception and selected refactoring legacy files first. Every leaf is at most 15 minutes own work; split before expanding. New or materially changed Python files must meet the applicable <=200 physical-line target and small cohesive unit boundaries; no mixin/namespace class or imported-method facade substitutes for responsibility decomposition. Preserve the pinned C901/format/lint and applicable typing baseline. Use the locked Project virtual environment, disable bytecode writes and keep disposable test state below configured Project Temporary State. Do not revert other workers' changes. One Task per file, exact predecessor history; review/update dependants after each completed Task.

Accepted request/pin extraction: canonical SelectedRouteError and all historic definitions remain import-compatible. Exact malformed versus stale definition_manifest failures are preserved and covered by a new functional regression test. The query admission mapping is externalized as an exact tuple-of-dicts JSON value and duplicate definition sequencing was removed. Independent architecture re-review closed all three findings. No terminal semantics or current manifest admission changed.

### Definition of Done

Retain actual before/after focused tests, changed paths, source/unit/complexity measurements and explicit unresolved limits. Preserve frozen test oracle bytes and current public behavior before new shared-context feature work. No production MCP, release, deployment, full suite, source-policy edits or Git publication.
