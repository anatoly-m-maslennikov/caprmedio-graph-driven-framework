---
atom_id: CA-R-1980
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings.Framework Control-Root Locator
relations:
  child_of:
  - CA-R-1176
version: 9
updated_at: 2026-10-27 20:00:06 +0400
tier: 3
type: Definition
---
# Summary

Define Project.Framework Settings.Framework Control-Root Locator

## Scope

the Project's framework control-root reference in Framework Settings.

## Claim

Framework Control-Root Locator **means** the Framework Settings reference to the Project's governed framework control directory.

## Details

Evidence: CA-D-370 requires the locator to resolve to the Directory Carrier prescribed by CA-D-317 without selecting another authority root. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no path or alternative authority root; those remain Delivery rules.
