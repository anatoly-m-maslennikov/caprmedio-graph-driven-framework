---
atom_id: CA-R-1982
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Continuant/Project.Framework Settings.Interaction
relations:
  child_of:
  - CA-R-1176
version: 1
updated_at: "2026-10-17 17:47:39 +0400"
---
# Summary

Define Project.Framework Settings.Interaction

## Scope

the Interaction grouping in the Project's Framework Settings.

## Claim

Interaction **means** the group of Framework Settings choices that govern presentation of information to the Operator.

## Details

Evidence: CA-R-1628 defines reporting-mode values; CA-R-1439 limits effects to presentation; CA-R-1440 preserves mandatory information. These define the child setting and its constraints, not the parent grouping. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This grouping adds no authorization, workflow, validation or safety behavior.
