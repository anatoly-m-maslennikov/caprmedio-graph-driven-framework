---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-1711
atom_id: CA-R-1651
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Propose Development Backlog splits

## Claim

### Prose Claim


a Development Backlog Epic that **contains** **`>50`** Task Atoms.


Governance **must** propose narrower ordered Epics **and** **may** apply the split **only** **after** Operator approval.
