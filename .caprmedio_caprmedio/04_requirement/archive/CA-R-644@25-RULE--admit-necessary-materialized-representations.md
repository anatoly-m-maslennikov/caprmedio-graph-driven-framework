---
atom_id: CA-R-644
ref_id: CA-R-644@25
container:
  scope_unit: CA-SU-00
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Project
tier: 1
relations:
  child_of:
  - CA-M-446
status: archived
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-644@25-RULE--admit-necessary-materialized-representations.md
    path: .caprmedio_caprmedio/04_requirement/archive
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: permission
current_scope_unit: caprmedio
---
## Summary

Admit necessary materialized representations

## Claim

### Prose Claim


CAPRMEDIO **may** admit a materialized representation **only** **when** an explicit Requirement establishes that the representation is necessary **to** preserve a required outcome **or** a material governed distinction under CA-M-005.

possible justifications include:

- an external contract;
- portability;
- performance;
- availability;
- an audit snapshot; **or**
- independently usable publication.

these examples do **not** close the set of justifications; another justification still requires the explicit Requirement **and** demonstrated necessity.
