---
subjects:
  active: Entity/Aspect/Engineering/Data Handling/Source Selection
  passive: []
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-686
  depends_on:
  - CA-R-1502
  - CA-R-1698
atom_id: CA-R-1769@33
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
tier: 2
role: Requirement
form: Rule
---
## Summary

Select Methodology Source revisions explicitly

## Claim scope

Methodology Source updates or downgrades applied by a Project.

## Claim

a Project **must** apply a Methodology Source update **or** downgrade **only** by selecting an identified source revision **and** reconciling affected Project authority; the selection **must not** silently rewrite other Methodology Sources **or** Project-owned Atoms.
