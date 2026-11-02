---
subjects:
  governs: Entity/Aspect/Engineering/Data Handling/Source Selection
  depends_on: []
version: 32
updated_at: 2026-10-29 10:13:51 +0400
relations:
  child_of:
  - CA-R-686
  depends_on:
  - CA-R-1502
  - CA-R-1698
atom_id: CA-R-1769@32
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Select Methodology Source revisions explicitly

## Claim scope

Methodology Source updates or downgrades applied by a Project.

## Claim

a Project **must** apply a Methodology Source update **or** downgrade **only** by selecting an identified source revision **and** reconciling affected Project authority; the selection **must not** silently rewrite other Methodology Sources **or** Project-owned Atoms.
