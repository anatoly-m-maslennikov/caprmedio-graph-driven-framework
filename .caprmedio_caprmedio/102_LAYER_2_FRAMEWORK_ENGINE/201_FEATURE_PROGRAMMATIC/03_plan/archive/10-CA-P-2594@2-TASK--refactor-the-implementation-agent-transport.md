---
atom_id: CA-P-2594@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
version: 2
updated_at: '2026-10-22T09:59:19Z'
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

Refactor the implementation Agent transport

## Objective

Decompose the 425-line transport by response contract, workspace/effect observation and bounded process lifecycle. Preserve public API, cancellation, diagnostics, timeouts, source/output limits and capability checks; add no new result labels before the refactor passes.

## Details

The Operator explicitly refused a source-size exception and selected refactoring legacy files first. Every leaf is at most 15 minutes own work; split before expanding. New or materially changed Python files must meet the applicable <=200 physical-line target and small cohesive unit boundaries; no mixin/namespace class or imported-method facade substitutes for responsibility decomposition. Preserve the pinned C901/format/lint and applicable typing baseline. Use the locked Project virtual environment, disable bytecode writes and keep disposable test state below configured Project Temporary State. Do not revert other workers' changes. One Task per file, exact predecessor history; review/update dependants after each completed Task.

Verified refactor: implementation_agent.py is 135 physical lines; cohesive contracts, workspace and transport modules are 179, 125 and 171. Maximum executable unit is 22 logical lines. Worker reports transport 7/7, selected-provider transport 2/2 and Docker transport-boundary 8/8 passing; Ruff, C901 and format pass. Independent read-only review found no blocking behavior/API regression and verified capability, source/output, timeout and effect-observation preservation. Dockerfile carries the whole Engine tree; no explicit module copy list is missing the new carriers. Existing public imports and patch points remain compatible. No new result labels or shared-context behavior were introduced. Existing unrelated CA-R-1843 freshness failure is not refactor acceptance evidence; unchanged process-log bounding and process-group timeout-race risks are not claimed fixed.

### Definition of Done

Retain actual before/after focused tests, changed paths, source/unit/complexity measurements and explicit unresolved limits. Preserve frozen test oracle bytes and current public behavior before new shared-context feature work. No production MCP, release, deployment, full suite, source-policy edits or Git publication.
