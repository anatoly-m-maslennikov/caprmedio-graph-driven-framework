---
identity:
  atom_id: CA-E-642@15
  ref_id: CA-E-642@15
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Coverage
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Coverage
  tier: 5
relations:
  evaluation_for:
  - CA-M-424
  - CA-M-395
state:
  status: Archived
  version: 15
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-E-642@15-PROGRAMMATIC-DIRECT_POLICY--evaluate-active-method-coverage.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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
