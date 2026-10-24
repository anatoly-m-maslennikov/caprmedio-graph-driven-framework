---
atom_id: CA-E-637@4
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Subject/Engineering/Evaluation Technique Selection
  depends_on: []
relations: {}
tier: 1
---
# Summary

Require observable evidence for behavioral acceptance

## Scope

The foundational evidence boundary for behavioral software Evaluation of PROGRAMMATIC components.

## Claim

Given the applicable Spec and declared failure predicates, behavioral software Evaluation **may** support acceptance **only when** **every** predicate is covered by **`>=1`** reproducible check. No check **may** make acceptance depend solely on replaceable private Implementation structure **when** a semantic **or** public behavior boundary can expose the predicate.

## Details

These necessary evidence conditions do not select a portfolio, cost ranking or fixed test-scope ratio.

## Sources

- [CA-E-389@11 — historical extraction basis](archive/CA-E-389-PROGRAMMATIC-CORE-EVAL_APPROACH--combine-complementary-software-behavior-evidence@11.md)
