---
atom_id: CA-P-2595@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
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
  - CA-P-2577
  depends_on:
  - CA-P-2590
  - CA-P-2593
  - CA-P-2594
  relates_to:
  - CA-P-2577
  - CA-E-539
tier: 3
---
# Summary

Review the behavior-preserving native refactor

## Objective

Independently verify the three legacy refactors against preserved frozen behavior, API/import compatibility and current source size/complexity/typing guidance. Update dependent native Tasks before authorizing feature changes.

## Details

The Operator explicitly refused a source-size exception and selected refactoring legacy files first. Every leaf is at most 15 minutes own work; split before expanding. New or materially changed Python files must meet the applicable <=200 physical-line target and small cohesive unit boundaries; no mixin/namespace class or imported-method facade substitutes for responsibility decomposition. Preserve the pinned C901/format/lint and applicable typing baseline. Use the locked Project virtual environment, disable bytecode writes and keep disposable test state below configured Project Temporary State. Do not revert other workers' changes. One Task per file, exact predecessor history; review/update dependants after each completed Task.

Reviewed predecessor: CA-P-2594 is Done after 17 focused checks and independent Agent refactor review. Its four files satisfy the source/unit/complexity limits and preserve existing transport labels and public imports. Route and executor predecessors remain required; partial predecessor success does not admit feature changes. Keep the known pre-existing freshness/Journal baseline failures separate from any new refactor regression.

Route predecessor CA-P-2591 and its two contained Tasks are now Done after the three review findings were corrected, focused suites and strict Mypy15 passed, and independent re-review accepted preserved public behavior. Root measured all15 source files below200 lines and no logical unit above40; permitted26–40-line functions retain single cohesive jobs. Only executor predecessor CA-P-2590 remains required. This gate stays Backlog; do not resume feature changes from partial refactor success or accept in-flight executor compatibility regressions.

### Definition of Done

Retain actual before/after focused tests, changed paths, source/unit/complexity measurements and explicit unresolved limits. Preserve frozen test oracle bytes and current public behavior before new shared-context feature work. No production MCP, release, deployment, full suite, source-policy edits or Git publication.

### Refactor gate checkpoint — 22 October 2026

Accept the behavior-preserving refactor-first gate after CA-P-2590, CA-P-2593 and CA-P-2594 complete. Final independent source and behavioral test-seam reviews returned PASS; all concrete graph/public-export regressions were repaired and their Concerns resolved. The stable 83-file candidate passes real pinned Ruff format/lint/C901, strict Mypy, <=200 physical file lines and <=40 logical unit lines (maximum 38). Candidate digest: 867c1ca1f5df727c6143d4742d1ebf5937b0acbb218c0768c0ec28149eb9f456. Canonical profile digest: 282e62e809eff157ecebeca6418ec12031914117e287b3fc7826004bb89d5c72. Current Method projection covers exactly 39 Active root Methods and their hashes match current sources. Unchanged oversized container source, unchanged test complexity and the narrow legacy MCP confirmation import are not newly admitted strict-source targets or hidden exceptions. New Workflow feature Tasks may now resume; runtime admission, full suite, commit, release and deployment remain separate and unperformed.
