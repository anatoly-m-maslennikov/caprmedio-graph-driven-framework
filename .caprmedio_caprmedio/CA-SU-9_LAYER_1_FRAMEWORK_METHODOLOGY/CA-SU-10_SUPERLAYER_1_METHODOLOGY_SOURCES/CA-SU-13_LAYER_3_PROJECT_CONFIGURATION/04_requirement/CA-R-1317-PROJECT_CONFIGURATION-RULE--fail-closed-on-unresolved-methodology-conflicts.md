---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form:=Applicable Methodology)
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Scope Unit
version: 31
updated_at: 2026-11-02 08:06:47 +0400
atom_id: CA-R-1317
ref_id: CA-R-1317
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-13
carrier_destination:
  file:
    name: CA-R-1317-PROJECT_CONFIGURATION-RULE--fail-closed-on-unresolved-methodology-conflicts.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
---
## Summary

Fail Closed on Unresolved Methodology Conflicts

## Claim

### Prose Claim


unresolved conflicts in Applicable Methodology **and** their required Operator approvals.


**if** an Applicable Methodology conflict remains unresolved **or** its required Operator approval is missing, stale, partial, ambiguous, **or** mismatched, **then** compilation **must** fail **without** changing Applicable Methodology membership.

## Details

qualifying approval **must** be the Operator's unambiguous current decision bound **to** the exact proposal, conflict, **and** source-frontier digest under CA-O-007 and CA-O-011, independently retained **and** verified through admitted execution evidence. a Journal append remains a business-provenance obligation; its failure yields a `recording_error` diagnostic and is not a prerequisite, proof, permission, completion, **or** recovery gate. a Project Configuration approval Atom, an LLM judgment, **or** inferred intent **must not** substitute for that decision **or** bypass the Core expansion boundary.
