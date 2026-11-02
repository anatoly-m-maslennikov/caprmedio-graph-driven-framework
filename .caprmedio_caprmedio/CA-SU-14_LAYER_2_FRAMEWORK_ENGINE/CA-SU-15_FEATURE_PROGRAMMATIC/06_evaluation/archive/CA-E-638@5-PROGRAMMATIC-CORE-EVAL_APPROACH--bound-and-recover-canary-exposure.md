---
atom_id: CA-E-638@5
content_role: Evaluation
type: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 01:50:12 +0400
subjects:
  governs: Subject/Engineering/Evaluation Technique Selection
  depends_on: []
relations: {}
tier: 1
---
# Summary

Bound and recover canary exposure

## Scope

Canary Evaluation of a changed PROGRAMMATIC component against a production-like or live workload.

## Claim

Canary Evaluation **may** be admitted **only when** the cohort **or** shadow surface isolates exposure; exposure is bounded; immediate stop is available; **and** rollback has been tested against the applicable state boundary. Canary evidence supplements rather than replaces required pre-deployment evidence.

## Details

These are necessary safety conditions, not a complete canary technique specification.

## Sources

- [CA-E-536@2 — historical extraction basis](archive/CA-E-536-PROGRAMMATIC-CORE-EVAL_APPROACH--admit-safe-canary-evaluation@2.md)
