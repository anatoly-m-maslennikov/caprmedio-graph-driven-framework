---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
version: 31
updated_at: 2026-11-02 00:18:22 +0400
relations:
  depends_on:
  - CA-R-1708
atom_id: CA-R-1711
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Classify Development Backlog as Epic

## Claim scope

Development Backlog and its Epic classification.

## Claim

the caprmedio Project **must** classify the Development Backlog as an Epic whose direct Task members are accepted intended actions that have no narrower Epic.
