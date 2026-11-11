---
atom_id: CA-R-024
ref_id: CA-R-024
container:
  scope_unit: CA-SU-00
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  - CAPRMEDIO_MODEL <+ Atom
tier: 2
status: Active
version: 29
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-024-CAPRMEDIO-RULE--govern-requirement-conflicts-by-tier.md
    path: .caprmedio_caprmedio/04_requirement
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: obligation
current_scope_unit: caprmedio
---
## Summary
Govern Requirement conflicts by tier

## Claim

### Prose Claim


CAPRMEDIO **must** resolve conflicts among active Requirements other than Requirements expressing Project-wide foundational invariants through explicit rules determined by their applicability tiers rather than presentation order, Concern priority, **or** implicit interpretation.
