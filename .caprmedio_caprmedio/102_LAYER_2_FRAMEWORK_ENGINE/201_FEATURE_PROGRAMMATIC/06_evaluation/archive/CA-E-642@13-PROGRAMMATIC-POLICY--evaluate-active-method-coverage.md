---
atom_id: CA-E-642@13
content_role: Evaluation
type: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Verification/Test Design
  depends_on:
  - Subject/Graph Node/Engineering/Verification/Coverage
relations:
  evaluation_for:
  - CA-M-424
  - CA-M-395
tier: 5
---
# Summary

Evaluate active Method coverage

## Scope

Evaluation-portfolio selection and change-readiness assessment under CA-M-424 and CA-M-395, over the complete applicable Active Method universe at Core, General and Standard tiers. Include relevant descendant-scope policies for the bounded implementation surface.

## Claim

Accept a portfolio or readiness assessment as complete only when every applicable Active Method obligation has a substantive Evaluation and current evidence selected for its failure mode. Definition coverage alone is not performed implementation conformance. A relation to an Evaluation is routing metadata, not evidence and not proof of coverage. Record each obligation as covered, partial, uncovered or inapplicable, with the evidence or reason. This portfolio mapping does not create an additional release gate.

## Details

- Derive the applicable Method set from current authority and the actual changed or delivered surface.
- Use static checks, functional or integration tests, end-to-end or canary checks, and focused review according to the failure mode.
- Permit one Evaluation to cover many Methods and one Method to be covered by many Evaluations when each link names the substantive predicate; do not count links or projections as evidence.
- Mark missing fixtures, unavailable environments, contradictory authority or insufficient observations unresolved or partial, not passing. Recompute when the Method, implementation surface or Evaluation changes.
