---
atom_id: CA-P-2590@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 6
updated_at: 2026-10-24 10:35:14 +0400
subjects:
  governs: Subject/Engineering/Implementation Evaluation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2585
  depends_on:
  - CA-P-2586
  - CA-P-2587
  - CA-P-2588
  - CA-P-2589
  relates_to:
  - CA-P-2577
  - CA-E-539
tier: 3
---
# Summary

Verify the bounded selected execution public owner

## Objective

Keep the public SelectedExecution interface and current consumers compatible, verify source-size/complexity boundaries and focused frozen behavior, and report any remaining oversized responsibility before native features resume.

## Details

The Operator explicitly refused a source-size exception and selected refactoring legacy files first. Every leaf is at most 15 minutes own work; split before expanding. New or materially changed Python files must meet the applicable <=200 physical-line target and small cohesive unit boundaries; no mixin/namespace class or imported-method facade substitutes for responsibility decomposition. Preserve the pinned C901/format/lint and applicable typing baseline. Use the locked Project virtual environment, disable bytecode writes and keep disposable test state below configured Project Temporary State. Do not revert other workers' changes. One Task per file, exact predecessor history; review/update dependants after each completed Task.

Final integration depends on all four extracted responsibilities, not just the graph-loop leaf. Preserve public imports and all production caller behavior; migrate private incidental test seams to canonical owners without altering frozen data or assertions. Accept only after every materially changed file/unit satisfies source guidance, strict admitted typing passes, related legacy behavior is green and independent review closes regressions. The existing Journal-boundary fixture failure was reproduced as missing explicit recording context: the same five tests pass when the fixture supplies author/timezone and Project-local temporary paths; test-only correction is separately owned, not a production Journal policy change.

### Dependency review — 22 October 2026

CA-P-2589 is reviewed Done and CA-C-577 is Resolved for the bounded canonical graph modules; this does not accept the public integration. Preserve its recovery, revisit, exact-diagnostic and final-write regressions in the final focused portfolio. Reconciliation has separate zero-write and write-order tests.

The legacy executor fixture currently fails because its isolated manifest-reader seam is bypassed by direct canonical graph validation after extraction, not because its golden source data should be refreshed. Preserve admission checks and the frozen oracle while migrating only the incidental injection seam to its canonical owner. The shared tracker must also preserve the Subject-batch route instead of bypassing it through a direct graph-only callback. Consolidate lifecycle dispatch to one typed owner; canonical helper results must pass through unchanged. Final acceptance requires these integration closures and the complete related focused evidence, not the partial 73-file strict-typing checkpoint.

### Definition of Done

Retain actual before/after focused tests, changed paths, source/unit/complexity measurements and explicit unresolved limits. Preserve frozen test oracle bytes and current public behavior before new shared-context feature work. No production MCP, release, deployment, full suite, source-policy edits or Git publication.

### Refactor gate checkpoint — 22 October 2026

The public stateful executor is 197 formatted lines rather than 2,856; selected routes are 126 rather than 1,081, and Agent transport is 135 rather than 425. Public error/Run-ID exports are preserved from canonical contracts. CA-C-577, CA-C-578 and CA-C-579 are Resolved with focused regressions and peer review. The complete executor baseline passed 23/23, Subject-batch execution 7/7, graph completion 12/12, lifecycle composition 7/7, container composition 5/5, MCP routes 21/21, the new MCP error consumer 1/1 and queue repair 5/5. Frozen data and behavioral assertions were preserved. All 83 admitted bounded files pass strict Mypy and pinned Ruff format/lint/C901, all are <=200 physical lines, and the largest tokenized logical unit is 38. Independent reviews accepted cohesive 26–40 units. No exception was used.
