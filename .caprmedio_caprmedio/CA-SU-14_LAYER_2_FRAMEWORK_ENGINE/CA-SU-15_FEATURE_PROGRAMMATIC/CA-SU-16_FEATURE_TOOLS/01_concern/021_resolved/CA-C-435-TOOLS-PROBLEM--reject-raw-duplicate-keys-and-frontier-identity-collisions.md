---
atom_id: CA-C-435
ref_id: CA-C-435
container:
  scope_unit: CA-SU-16
role: Concern
form: Problem
topics:
  main_subject: Journal raw identity validation
  dependencies:
  - Subject/Domain/Node/Continuant/History/Journal
  - Event
  - QUERY_FILTER
relations:
  relates_to:
  - CA-R-1861
  - CA-R-1865
  - CA-M-334
  - CA-E-577
status: resolved
version: 2
updated_at: 2026-10-23 03:14:50 +0400
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-C-435-TOOLS-PROBLEM--reject-raw-duplicate-keys-and-frontier-identity-collisions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/01_concern/021_resolved
---
# Summary

Reject raw duplicate keys and frontier identity collisions

## Disposition

Resolved in the Journal source contract: raw JSON duplicate object keys are
rejected before parse, and Event IDs must be unique across the captured frontier.
CA-E-577 preserves expected-failure evidence; no implementation claim is made.
