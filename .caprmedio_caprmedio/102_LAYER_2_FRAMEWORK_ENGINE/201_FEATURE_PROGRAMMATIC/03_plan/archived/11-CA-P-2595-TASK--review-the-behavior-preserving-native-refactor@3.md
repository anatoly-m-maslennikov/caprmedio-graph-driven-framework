---
atom_id: CA-P-2595
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
version: 3
updated_at: "2026-10-22T10:22:32Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2577]
  depends_on: [CA-P-2590, CA-P-2593, CA-P-2594]
  relates_to: [CA-P-2577, CA-E-539]
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
