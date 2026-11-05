---
version: 1
updated_at: 2026-11-02 19:32:45 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-M-447
  - CA-R-1407
cce_version: cce_1
cce_form: obligation
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.order.number
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-2691
ref_id: CA-R-2691
tier: 1
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-R-2691-CAPRMEDIO-RULE--keep-nesting-and-sibling-order-distinct.md
    path: .caprmedio_caprmedio/04_requirement
---
## Summary

Keep nesting and sibling order distinct

## Claim

### Prose Claim


Scope Unit parentage and order among siblings are different. An ordered unit’s number is its position among ordered siblings with the same direct parent.

Dependency permission follows its relation-family rules. A filename number, nesting position or the assumption that every Scope Unit is a Layer does not create that permission.
