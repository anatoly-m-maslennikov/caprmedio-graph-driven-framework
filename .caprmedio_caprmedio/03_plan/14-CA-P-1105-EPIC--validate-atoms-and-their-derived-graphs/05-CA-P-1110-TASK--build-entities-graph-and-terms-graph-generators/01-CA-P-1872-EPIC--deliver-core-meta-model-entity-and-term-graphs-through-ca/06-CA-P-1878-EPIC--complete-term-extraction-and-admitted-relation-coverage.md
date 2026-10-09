---
atom_id: CA-P-1878
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Projection
  depends_on:
    - Entity
    - Term
    - Atom
    - Property
    - Scope Unit
    - Tool
    - MCP
    - Workflow
    - Action
    - Journal
    - Plan
version: 1
updated_at: "2026-10-09 17:13:17 +0400"
relations:
  is_decomposition_of:
    - CA-P-1872
  blocks:
    - CA-P-1883
    - CA-P-1884
---
# Summary

Complete term extraction and admitted relation coverage

## Objective

Complete the bounded child work for term extraction and admitted relation coverage.

## Details

Own work: none. This group is complete only through its direct child Plans.

Direct children:

- [CA-P-1879](06-CA-P-1878-EPIC--complete-term-extraction-and-admitted-relation-coverage/01-CA-P-1879-TASK--implement-current-term-hierarchy-extraction.md) — Implement current term hierarchy extraction.
- [CA-P-1880](06-CA-P-1878-EPIC--complete-term-extraction-and-admitted-relation-coverage/02-CA-P-1880-TASK--check-admitted-relation-coverage-and-record-bounded-gaps.md) — Check admitted relation coverage and record bounded gaps.

Any required relation gap gets a separately admitted bounded direct child before implementation and blocks the golden fidelity Task. This group cannot finish while a required gap remains.

Inherited safeguards: the main Epic's current source authority, graph separation, Property ownership, owned-Core selection, runtime identity and truthful evidence apply. Keep CA-P-1110's inherited 99% confidence threshold.

### Definition of Done

the Plan is **not** Done **if** ((any direct child is **not** Done) **or** (required group evidence is missing, blocked, failed, stale **or** conflicting) **or** (a required relation gap is unresolved **or** lacks its admitted bounded child)).
