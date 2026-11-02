---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery/Type'
  depends_on: []
version: 32
updated_at: 2026-10-29 07:45:30 +0400
relations: {}
atom_id: CA-R-1665@32
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Rule
tier: 3
---
## Summary

Register Type Values for Delivery Atoms

## Claim scope

`Atom/Content Role: Delivery/Type` values.

## Claim

Eng Policy and Eng Decision **must** be registered as internal values of `Atom/Content Role: Delivery/Type`. Release Definition and Environment Definition remain registered outside PROGRAMMATIC and its descendants.

## Details

Eng Policy and Eng Decision are defined by CA-R-2121 and CA-R-2122. Within PROGRAMMATIC and its descendants, Delivery Atoms use only those two Types. Existing specific Delivery Types remain valid outside that scope where their meanings apply. Registration does not constrain a Type value to a particular Tier.
