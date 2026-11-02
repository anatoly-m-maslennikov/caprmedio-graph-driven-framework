---
subjects:
  active: Aspects <+ Engineering
  passive: []
version: 14
updated_at: 2026-11-02 18:35:20 +0400
relations:
  depends_on:
  - CA-O-058
  - CA-R-1702
atom_id: CA-R-1795@14
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
tier: 4
role: Requirement
form: Rule
---
## Summary
Reconcile Development Backlog candidates **after** release

## Claim scope
Development Backlog candidates **after** a Release Record is accepted.

## Claim

CAPRMEDIO **must** reconcile the Development Backlog against its exact released manifest as follows:

- remove a candidate whose promoted Atoms were fully delivered **in** that release.
- **every** candidate that is unfinished, partially delivered, excluded, **or** newly deferred **must** remain unscheduled **or** move **to** another target version.
- a candidate **must not** be removed as shipped **unless** the released manifest accounts for its promoted Atoms.
