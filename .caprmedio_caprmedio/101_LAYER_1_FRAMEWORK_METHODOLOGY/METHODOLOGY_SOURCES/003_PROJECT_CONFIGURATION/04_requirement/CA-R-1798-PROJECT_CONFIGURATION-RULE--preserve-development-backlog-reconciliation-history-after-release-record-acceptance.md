---
subjects:
  governs: Subject/Graph Node/Engineering
  depends_on: []
version: 8
updated_at: 2026-10-25 17:32:27 +0400
relations:
  depends_on:
  - CA-O-058
  - CA-R-1702
atom_id: CA-R-1798
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
tier: 4
type: Rule
---
# Summary
Preserve Development Backlog reconciliation history **after** Release Record acceptance

## Scope
released, executed, **and** planning-allocation history from Development Backlog reconciliation **after** the Release Record is accepted.

## Claim

CAPRMEDIO **must** preserve delivered work, executed work, **and** planning-allocation changes **in** Release Records, Plans under `done/`, **and** Git history.

## Details
