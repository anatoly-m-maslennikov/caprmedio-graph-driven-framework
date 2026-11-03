---
subjects:
  active: CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering
version: 16
updated_at: 2026-11-02 19:44:26 +0400
relations:
  depends_on:
  - CA-O-058
  - CA-R-1702
atom_id: CA-R-1798
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 4
role: Requirement
form: Rule
---
## Summary
Preserve Development Backlog reconciliation history **after** Release Record acceptance

## Claim scope
released, executed, **and** planning-allocation history from Development Backlog reconciliation **after** the Release Record is accepted.

## Claim

CAPRMEDIO **must** preserve delivered work, executed work, **and** planning-allocation changes **in** Release Records, Plans under `done/`, **and** Git history.
