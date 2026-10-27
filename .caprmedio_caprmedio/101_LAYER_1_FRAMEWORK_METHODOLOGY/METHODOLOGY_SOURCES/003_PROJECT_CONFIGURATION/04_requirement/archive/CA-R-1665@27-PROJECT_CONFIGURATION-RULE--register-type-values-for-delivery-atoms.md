---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery/Type'
  depends_on: []
version: 27
updated_at: 2026-10-24 11:58:20 +0400
relations:
  child_of:
  - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
atom_id: CA-R-1665@27
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Rule
tier: 3
---
# Summary

Register Type Values for Delivery Atoms

## Scope

`Atom/Content Role: Delivery/Type` values.

## Claim

Eng Policy and Eng Decision **must** be registered as internal values of `Atom/Content Role: Delivery/Type`. Release Definition and Environment Definition remain registered outside PROGRAMMATIC and its descendants.

## Details

Eng Policy and Eng Decision are defined by CA-R-2121 and CA-R-2122. Within PROGRAMMATIC and its descendants, Delivery Atoms use only those two Types. Existing specific Delivery Types remain valid outside that scope where their meanings apply. Registration does not constrain a Type value to a particular Tier.
