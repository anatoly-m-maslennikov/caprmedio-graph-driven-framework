---
atom_id: CA-E-646
content_role: Evaluation
type: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 19:59:38 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring
  depends_on: []
relations:
  evaluation_for:
  - CA-M-421
tier: 4
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
