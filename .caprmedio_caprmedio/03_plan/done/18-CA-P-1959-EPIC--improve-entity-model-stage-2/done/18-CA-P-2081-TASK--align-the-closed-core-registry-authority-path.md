---
atom_id: CA-P-2081
content_role: Plan
type: Plan
label: Task
work_sequence_number: 18
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Subject
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Relation
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/Continuant/Tool
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 7
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1959
tier: 3
---
# Summary

Align the closed Core registry authority path

## Objective

The existing closed registry reads its unchanged relation authorities from the current declared Core folder.

## Details

Estimated own work: at most 15 minutes. This independent implementation repair does not depend on the unanswered selector choice. Applicable current Project Structure and graph contracts already bind the Core Meta-model authoring source; no authority semantics or RMEDO revision is required.

The focused registry test currently fails with registry-core-authority-path-unsupported. Read-only investigation verified all nine existing source pins at the current 101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL path. Substitution of that single closed path compiles only the existing three registered kinds.

Edit only GENERATE_ENTITY_GRAPH/core_relation_registry.py and its test_core_relation_registry.py fixture/regressions. Update the one closed authority-path constant to the exact current declaration. Keep exact declaration equality, Core ownership, source-byte/revision pins, foreign-path rejection and no-follow guards. Do not accept arbitrary roots, preserve a retired current-root fallback, widen kinds, change Subjects, admit selectors or mass-rewrite other legacy fixtures. No Core, runtime, MCP/FPF or live graph publication.

Verify the focused current-frontier case, foreign path/symlink rejection and downstream/full graph suites. Root owns Plan lifecycle, receipt and Git. Workers are not alone; preserve all other edits.

### Completion

The closed path now matches the current Project Structure. Independent review found no blocking issue; Root ran all 219 graph tests successfully. The nine source pins, three registered kinds and foreign/symlink rejection are unchanged. The retired root now has an explicit failing-closed regression. Original Core sources were not edited. Evidence: `_projection/core-entity-review/stage2/task-2081.receipt.json`.

### Definition of Done

Not Done if the current frontier fails, accepted roots or native kinds expand, pinned source authority changes, path/symlink failures are masked, tests fail, or own work exceeds 15 minutes without decomposition.
