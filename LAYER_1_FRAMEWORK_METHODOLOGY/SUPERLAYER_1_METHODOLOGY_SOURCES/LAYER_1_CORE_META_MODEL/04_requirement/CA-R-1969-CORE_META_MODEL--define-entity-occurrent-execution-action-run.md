---
atom_id: CA-R-1969
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Occurrent/Execution/Action Run"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-19 15:54:13 +0400"
---
# Summary

Define Entity/Occurrent/Execution/Action Run

## Scope

Actual executions of Actions.

## Claim

an Action Run **means** **`=1`** actual execution of **`=1`** Action. it is distinct from the Action definition **and** from records describing the execution.

## Details

Candidate #6 keeps Action definitions and actual Action Runs separate. CA-R-1452 defines the reusable Action. CA-R-853 governs Action Run attribution and authorization, but does not define Action Run itself.

 Action Run already has a governing R constraint in CA-R-853; the missing part is its substantive definition.
