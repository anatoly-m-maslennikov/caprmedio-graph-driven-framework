---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Applicable Methodology'
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Domain/Node/Continuant/Scope Unit.Expansion Boundary
version: 21
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-O-007
  - CA-O-011
atom_id: CA-R-1317
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Fail Closed on Unresolved Methodology Conflicts

## Scope

unresolved conflicts in Applicable Methodology **and** their required Operator approvals.

## Claim

**if** an Applicable Methodology conflict remains unresolved **or** its required Operator approval is missing, stale, partial, ambiguous, **or** mismatched, **then** compilation **must** fail **without** changing Applicable Methodology membership.

## Details

qualifying approval **must** be the Operator's unambiguous current decision bound **to** the exact proposal, conflict, **and** source-frontier digest under CA-O-007 and CA-O-011, independently retained **and** verified through admitted execution evidence. a Journal append remains a business-provenance obligation; its failure yields a `recording_error` diagnostic and is not a prerequisite, proof, permission, completion, **or** recovery gate. a Project Configuration approval Atom, an LLM judgment, **or** inferred intent **must not** substitute for that decision **or** bypass the Core expansion boundary.
