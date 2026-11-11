---
atom_id: CA-R-1651
ref_id: CA-R-1651
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form := Plan)'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
tier: 3
relations:
  child_of:
  - CA-R-1711
status: Active
version: 33
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1651-PROJECT_CONFIGURATION-RULE--propose-development-backlog-splits.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Propose Development Backlog splits

## Claim

### Prose Claim


a Development Backlog Epic that **contains** **`>50`** Task Atoms.


Governance **must** propose narrower ordered Epics **and** **may** apply the split **only** **after** Operator approval.
