---
atom_id: CA-P-2594
ref_id: CA-P-2594
container:
  atom: CA-P-2577
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/MCP
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2577
  relates_to:
  - CA-P-2577
  - CA-E-539
status: Done
version: 6
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: 10-CA-P-2594-TASK--refactor-the-implementation-agent-transport.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/done
work_sequence_number: 10
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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
