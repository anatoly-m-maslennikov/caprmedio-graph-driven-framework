---
subjects:
  active: Projection/(.Form:=Applicable Methodology)
  passive:
  - Scope Unit//PROJECT_CONFIGURATION
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/History/Journal > Event Record
  - Scope Unit
version: 31
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1317
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1317-PROJECT_CONFIGURATION-RULE--fail-closed-on-unresolved-methodology-conflicts.md
  source_atom_id: CA-R-1317
  source_atom_revision: 31
  source_sha256: 53952c082eb9b754a95d16cd1bc1eef7349fa8b507a4702c6358ca32c4322c91
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Fail Closed on Unresolved Methodology Conflicts

## Claim scope

unresolved conflicts in Applicable Methodology **and** their required Operator approvals.

## Claim

**if** an Applicable Methodology conflict remains unresolved **or** its required Operator approval is missing, stale, partial, ambiguous, **or** mismatched, **then** compilation **must** fail **without** changing Applicable Methodology membership.

## Details

qualifying approval **must** be the Operator's unambiguous current decision bound **to** the exact proposal, conflict, **and** source-frontier digest under CA-O-007 and CA-O-011, independently retained **and** verified through admitted execution evidence. a Journal append remains a business-provenance obligation; its failure yields a `recording_error` diagnostic and is not a prerequisite, proof, permission, completion, **or** recovery gate. a Project Configuration approval Atom, an LLM judgment, **or** inferred intent **must not** substitute for that decision **or** bypass the Core expansion boundary.
