---
subjects:
  governs: lifecycle-traceability
  depends_on: []
version: 21
updated_at: 2026-10-24 00:38:25 +0400
relations:
  child_of:
  - CAPRMEDIO-REQU-686-CORE-REQUIREMENT--separate-core-extension-and-project-configuration-authority
  depends_on:
  - CA-R-1502
  - CA-R-1698
atom_id: CA-R-1769@21
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 2
---
# Summary

Select Methodology Source revisions explicitly

## Scope

Methodology Source updates or downgrades applied by a Project.

## Claim

a Project **must** apply a Methodology Source update **or** downgrade **only** by selecting an identified source revision **and** reconciling affected Project authority; the selection **must not** silently rewrite other Methodology Sources **or** Project-owned Atoms.

## Details
