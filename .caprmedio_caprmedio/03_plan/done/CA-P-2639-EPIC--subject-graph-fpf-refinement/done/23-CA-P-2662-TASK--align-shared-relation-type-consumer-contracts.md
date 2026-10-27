---
atom_id: CA-P-2662
content_role: Plan
type: Plan
label: Task
work_sequence_number: 23
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Relation
version: 1
updated_at: 2026-10-26 22:56:54 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Align shared Relation Type consumer contracts

## Objective

Correct the five remaining consumer clauses that prescribe graph-owned Relation Types; preserve legitimate graph-qualified contexts and applicable constraints.

## Details

The accepted correction was applied through reviewed Drafts, with normal predecessor archival.
Evidence: `.caprmedio_tmp/subject-alignment-closure/relations.json`,
`promotion.json`, `verify.final.json` and `graph/graph.subject-views.manifest.json`.
Independent source/lifecycle/protected-state and projection checks passed.
No new Run kind, relation, field, aggregation/retry/branch policy or implementation was added.
The established Plan Done/Canceled containment policy remains unchanged.

## Definition of Done

- The accepted source meaning and its directly affected consumers agree.
- Source Summaries, identities and unrelated requirements are preserved.
- Applied successors and predecessor archives match the reviewed packet.
- The four Subject views use current source pins and have zero unmapped Subjects.
- No runtime, code, full-suite, release, commit or push result is claimed.
