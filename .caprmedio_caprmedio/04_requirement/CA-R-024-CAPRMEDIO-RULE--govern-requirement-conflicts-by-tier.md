---
version: 29
updated_at: 2026-11-02 18:35:20 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern)
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  - CAPRMEDIO_MODEL <+ Atom
cce_version: cce_1
cce_form: obligation
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-024
ref_id: CA-R-024
tier: 2
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-R-024-CAPRMEDIO-RULE--govern-requirement-conflicts-by-tier.md
    path: .caprmedio_caprmedio/04_requirement
---
## Summary
Govern Requirement conflicts by tier

## Claim

### Prose Claim


CAPRMEDIO **must** resolve conflicts among active Requirements other than Requirements expressing Project-wide foundational invariants through explicit rules determined by their applicability tiers rather than presentation order, Concern priority, **or** implicit interpretation.
