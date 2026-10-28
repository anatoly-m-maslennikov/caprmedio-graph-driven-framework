---
atom_id: CA-R-1969
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Action Run
relations:
  child_of:
  - CA-R-1174
version: 9
updated_at: 2026-10-27 20:00:06 +0400
tier: 3
type: Definition
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
