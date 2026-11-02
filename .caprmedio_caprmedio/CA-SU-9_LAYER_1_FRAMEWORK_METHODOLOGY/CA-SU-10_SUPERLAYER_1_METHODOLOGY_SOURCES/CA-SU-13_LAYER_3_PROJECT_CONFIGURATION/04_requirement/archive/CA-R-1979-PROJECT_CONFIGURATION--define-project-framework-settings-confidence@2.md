---
atom_id: CA-R-1979
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Project.Framework Settings.Confidence"
relations:
  child_of:
  - CA-R-1176
version: 2
updated_at: "2026-10-18 03:34:58 +0400"
---
# Summary

Define Project.Framework Settings.Confidence

## Scope

the Confidence grouping in the Project's Framework Settings.

## Claim

Confidence **means** the group of Framework Settings defaults for the declared Confidence Thresholds.

## Details

Evidence: CA-R-1652 defines the necessary-information threshold default; CA-R-380 defines the semantic-resolution threshold default. These define the child settings, not the parent grouping. Candidate #6 decision 8 retains Settings as the default source, and decision 18 distinguishes Project settings from the framework's name. This grouping adds no threshold, override layer or mandatory value. Concrete CAPRMEDIO setting definitions belong in Project Configuration.
