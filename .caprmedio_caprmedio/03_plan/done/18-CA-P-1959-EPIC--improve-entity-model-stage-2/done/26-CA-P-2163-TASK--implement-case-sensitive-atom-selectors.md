---
atom_id: CA-P-2163
ref_id: CA-P-2163
role: Plan
form: Plan
label: Task
work_sequence_number: 26
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
topics:
  main_subject: Subject/Graph Node/Domain/Continuant/Atom
  dependencies:
  - Subject
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Domain/Continuant/History
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 6
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1959
  depends_on:
  - CA-P-2162
tier: 3
container:
  atom: CA-P-1959
carrier_destination:
  file:
    name: 26-CA-P-2163-TASK--implement-case-sensitive-atom-selectors.md
    path: .caprmedio_caprmedio/03_plan/done/18-CA-P-1959-EPIC--improve-entity-model-stage-2/done
---
# Summary

Implement case-sensitive Atom selectors

## Objective

The approved selector and metadata changes have the exact, verified effect assigned to this Task.

## Details

Own work: at most fifteen minutes; create bounded children if this own-work limit is exceeded. Implement the reviewed selector contract in shared syntax, structural lookup, sealed preview and internal graph parsing. Preserve the whole selector token and its owner identity; do not infer native admission. Atom and atom must remain distinct. Reject malformed/unknown/duplicate/mixed selectors, eval, wildcards and unsupported operators. Verify focused regression tests and preserve existing apply guard and stale-source checks. Own code only after CA-P-2162 passes.

Root owns Git, Plan lifecycle and shared Journal recording. Workers are not alone; preserve unrelated release changes. Scratch and caches stay in `.caprmedio_tmp`; use uv. No unsupported MCP/FPF, general migration framework, runtime/release activation or Step 2 body sweep.

### Completion

Implemented and independently reviewed the exact case-sensitive selector surface across syntax, existing lookup/preview and graph source readers. All418 combined tests passed with stable code pins, including YAML serialization and preserved owner identity; no original Subject migration was performed. Exact verification is recorded in `_projection/core-entity-review/stage2/task-2163.receipt.json`.

### Definition of Done

Not Done if the assigned effect is unverified, source pins are stale, Atom and atom are conflated, unrelated work changes, exact prior source history is lost, execution evidence is fabricated, or completion claims exceed the assigned increment.
