---
atom_id: CA-P-1878@7
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Subject
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Tool
  - Subject/Engineering/MCP
  - Subject/Engineering/Workflow
  - Subject/Engineering/Action
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 7
updated_at: 2026-10-24 11:01:18 +0400
relations:
  is_decomposition_of:
  - CA-P-1872
  blocks:
  - CA-P-1883
  - CA-P-1884
tier: 3
---
# Summary

Complete term extraction and admitted relation coverage

## Objective

Complete the bounded child work for term extraction and admitted relation coverage.

## Details

Own work: none. This group is complete only through its direct child Plans.

Direct children:

- [CA-P-1879](06-CA-P-1878@7-EPIC--complete-term-extraction-and-admitted-relation-coverage/01-CA-P-1879-TASK--implement-current-term-hierarchy-extraction.md) — Implement current term hierarchy extraction.
- [CA-P-1880](06-CA-P-1878@7-EPIC--complete-term-extraction-and-admitted-relation-coverage/02-CA-P-1880-TASK--check-admitted-relation-coverage-and-record-bounded-gaps.md) — Check admitted relation coverage and record bounded gaps.

Any required relation gap gets a separately admitted bounded direct child before implementation and blocks the golden fidelity Task. This group cannot finish while a required gap remains.

Inherited safeguards: the main Epic's current source authority, graph separation, Property ownership, owned-Core selection, runtime identity and truthful evidence apply. Keep the Operator's explicit 90% confidence threshold.

### Definition of Done

the Plan is **not** Done **if** ((any direct child is **not** Done) **or** (required group evidence is missing, blocked, failed, stale **or** conflicting) **or** (a required relation gap is unresolved **or** lacks its admitted bounded child)).
