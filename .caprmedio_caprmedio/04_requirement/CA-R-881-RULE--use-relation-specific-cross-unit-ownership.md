---
atom_id: CA-R-881
ref_id: CA-R-881
container:
  scope_unit: CA-SU-00
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Atom.Content
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)'
tier: 1
relations:
  child_of:
  - CA-R-1407
  - CA-M-447
status: Active
version: 35
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-881-CAPRMEDIO-RULE--use-relation-specific-cross-unit-ownership.md
    path: .caprmedio_caprmedio/04_requirement
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
---
## Summary

Use relation-specific cross-unit ownership

## Claim

### Prose Claim


cross-unit relation ownership **must** follow the applicable relation-family authority rather than a universal common-ancestor rule; a Demand **must** be owned by its Consumer Scope Unit under CA-R-932@37 **and** **must** constrain **only** the Producer result that Consumer is permitted **to** depend on, with the applicable ancestry **and** ordered-sibling restrictions preserved.
