---
atom_id: CA-E-646
ref_id: CA-E-646
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring
tier: 4
relations:
  evaluation_for:
  - CA-M-421
status: Active
version: 14
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-E-646-PROGRAMMATIC-POLICY--evaluate-suitable-established-reuse.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Evaluate suitable established reuse

## Scope

New PROGRAMMATIC libraries, mechanisms, adapters, parsers, serializers, concurrency and testing approaches.

## Claim

Accept a custom mechanism when proportional fit and dependency-cost evidence support it: an unmet declared need, a concrete benefit, or materially lower operational or maintenance risk can justify the choice. Prefer a well-adopted suitable library, approach or tool when it satisfies declared behavior; this is a fit decision, not a brand mandate. Ordinary choices do not require separate catalog paperwork.

## Details

- Compare established candidates when the choice is non-obvious or risk-bearing, considering behavior, compatibility, security, performance, licensing and maintenance.
- Verify the selected solution owns the required behavior and wrappers do not recreate a second semantic implementation.
- For custom code, record the concrete unmet need or benefit and the bounded custom surface when that rationale matters; routine choices need no separate form.
- Reject a custom mechanism justified only by novelty or preference when an established solution fits.
- Keep review proportional to consequence and dependency cost; revisit it when the governing assumptions change.
