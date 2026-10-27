---
atom_id: CA-P-2162@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 25
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on:
  - Subject
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Subject/Domain/Node/Continuant/History
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 12:44:21 +0400
relations:
  is_decomposition_of:
  - CA-P-1959
  depends_on:
  - CA-P-2161
tier: 3
---
# Summary

Align RMEDO for case-sensitive Atom selectors

## Objective

The approved selector and metadata changes have the exact, verified effect assigned to this Task.

## Details

Own work: at most fifteen minutes; create bounded children if this own-work limit is exceeded. Review and align only current Core selector grammar and current Engine Subject Tool RMEDO before code. Atom is the Entity type; atom(...) is case-sensitive selector syntax, not an alias or new Entity kind. Use only the approved named Atom ID or role/type qualification. Preserve Summary, Subjects, unrelated metadata/body and exact prior versions. Record actual grammar effects and pins. This is the approved selector-grammar exception, not mass Subject migration.

Root owns Git, Plan lifecycle and shared Journal recording. Workers are not alone; preserve unrelated release changes. Scratch and caches stay in `.caprmedio_tmp`; use uv. No unsupported MCP/FPF, general migration framework, runtime/release activation or Step 2 body sweep.

### Completion

Adopted and independently verified the14 exact approved Core/Engine selector-grammar revisions (15 exact body deltas), their predecessors and28 actual Journal records. Atom and atom remain case-distinct; ordinary Subjects and unrelated content are unchanged. Exact verification is recorded in `_projection/core-entity-review/stage2/task-2162.receipt.json`.

### Definition of Done

Not Done if the assigned effect is unverified, source pins are stale, Atom and atom are conflated, unrelated work changes, exact prior source history is lost, execution evidence is fabricated, or completion claims exceed the assigned increment.
