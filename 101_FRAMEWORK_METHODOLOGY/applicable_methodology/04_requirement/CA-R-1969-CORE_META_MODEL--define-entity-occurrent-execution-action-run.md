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
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1969-CORE_META_MODEL--define-entity-occurrent-execution-action-run.md
  source_atom_id: CA-R-1969
  source_atom_revision: 2
  source_sha256: 8fc7d48213c540944784de2f6b8ec1ee349f38965611f56692f7a8911f686008
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
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
