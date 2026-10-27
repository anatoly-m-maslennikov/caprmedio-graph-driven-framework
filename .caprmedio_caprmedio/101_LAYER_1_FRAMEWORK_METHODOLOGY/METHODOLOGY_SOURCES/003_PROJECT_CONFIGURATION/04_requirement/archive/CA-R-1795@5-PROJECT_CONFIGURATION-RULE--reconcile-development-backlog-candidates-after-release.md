---
subjects:
  governs: development-flow
  depends_on: []
version: 5
updated_at: 2026-10-24 11:58:20 +0400
relations:
  depends_on:
  - CA-O-058
  - CA-R-1702
atom_id: CA-R-1795@5
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 4
type: Rule
---
# Summary
Reconcile Development Backlog candidates **after** release

## Scope
Development Backlog candidates **after** a Release Record is accepted.

## Claim

CAPRMEDIO **must** reconcile the Development Backlog against its exact released manifest as follows:

- remove a candidate whose promoted Atoms were fully delivered **in** that release.
- **every** candidate that is unfinished, partially delivered, excluded, **or** newly deferred **must** remain unscheduled **or** move **to** another target version.
- a candidate **must not** be removed as shipped **unless** the released manifest accounts for its promoted Atoms.

## Details
