---
atom_id: CA-E-638
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-15 22:37:03 +0400"
subjects:
  governs: "programmatic canary exposure safety"
  depends_on: ["programmatic software", "Evaluation", "Implementation"]
relations: {}
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
