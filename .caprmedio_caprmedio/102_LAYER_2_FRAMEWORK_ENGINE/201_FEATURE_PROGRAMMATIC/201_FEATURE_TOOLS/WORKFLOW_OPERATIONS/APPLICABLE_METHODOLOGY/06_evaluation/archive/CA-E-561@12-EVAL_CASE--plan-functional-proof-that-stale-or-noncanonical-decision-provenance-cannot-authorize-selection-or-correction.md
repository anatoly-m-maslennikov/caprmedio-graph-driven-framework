---
atom_id: CA-E-561@12
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-24 13:39:34 +0400
subjects:
  governs: Tool/WORKFLOW_OPERATIONS/APPLICABLE_METHODOLOGY
  depends_on:
  - Subject/Engineering/Tool
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Methodology Source
  - Subject/Domain/Node/Continuant/Projection
relations:
  evaluation_for:
  - CA-R-2118
  - CA-R-1842
tier: 4
---
# Summary

Plan functional proof that stale or noncanonical decision provenance cannot authorize selection or correction.

## Scope

Functional approval-currentness and provenance cases for conflict selection and source correction.

## Claim

An implementation **must** reject every approval that is not the exact current actual Operator decision for the assessed source frontier with independently verified admitted Run and effect evidence. Journal references are optional observations and cannot authorize the approval by themselves.

## Details

Start from an assessed conflict and test a missing, stale-digest, mismatched-conflict, mismatched-proposal, mismatched-selected-source, ambiguous, rejected, revoked, or otherwise stale decision or independent Run/effect evidence. Each case must return `blocked`, name the failing provenance binding, create no source edit or output mutation, and preserve the prior output. A missing or failed Journal append alone must not block when the actual decision and independent evidence are valid. A TOML approval index alone, with or without a matching Journal record, must not authorize; it may pass only when it resolves the independently verified decision and effect evidence.

Then provide one exact Operator decision with independent Run/effect evidence, optional Journal observation, and source bindings, change one selected source, and assert that the old decision becomes stale and apply remains blocked until fresh selection and assessment. Assert that an external authorized source correction receipt likewise requires reselection/reassessment rather than enabling direct publication. This carrier records planned functional proof, not a runtime pass.

### Sources

- CA-R-2118; CA-R-1842; CA-O-155 v2; CA-O-156 v2; CA-P-1442 v1.
