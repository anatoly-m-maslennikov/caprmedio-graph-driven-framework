---
atom_id: CA-M-424@1
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Archived
subjects:
  governs: "Method/Evaluation Technique Selection"
  depends_on:
    - "Method/Specification Sufficiency"
    - "Entity/Node/Continuant/Actor"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  derived_from:
    - CA-A-053
  child_of:
    - CA-M-415
---
# Summary

Select software Evaluation techniques by failure mode

## Scope

selection of behavioral software Evaluation techniques for PROGRAMMATIC components.

## Claim

**to** select behavioral software Evaluation techniques for a PROGRAMMATIC component, the Actor selecting the portfolio **must** take the applicable Spec, declared failure predicates, **and** active Evaluation authority as inputs; identify candidate checks for **every** predicate; evaluate candidate portfolios against the applicable Core **and** General Evaluation policy **and** each selected technique's own acceptance **and** disposition rules; select one admitted portfolio; repeat **until** all predicates are covered **or** no candidate remains; produce the selected Evaluation identities **and** selection rationale; **and** return unresolved predicates for authority **or** design clarification **when** no portfolio is admitted.

## Details

Candidate source: [CA-M-285@14](archive/CA-M-285-PROGRAMMATIC--select-software-evaluation-techniques-by-failure-mode@14.md)

1. enumerate the failure predicates established by applicable authority **and** bind each predicate **to** the observable behavior that can distinguish acceptance from rejection.
2. identify applicable Evaluation Atoms across test scopes, purposes, boundary-realism choices, execution environments, **and** release stages **without** treating those labels as a universal ranking.
3. construct candidate portfolios from those Evaluation Atoms. include a specialized technique **only when** its Evaluation applicability **and** evidence preconditions are satisfied.
4. evaluate **every** candidate portfolio under the Core evidence invariant in CA-E-637, the General portfolio criteria in CA-E-389, **and** the acceptance **and** disposition rules of **every** selected Evaluation Atom. apply the Core exposure invariant in CA-E-638 **and** the General canary criteria in CA-E-536 **when** a candidate includes canary evidence.
5. stop with one traceable admitted portfolio **when** all predicates are covered. **when** no candidate passes, return the uncovered predicates, failed policy conditions, **and** missing evidence rather than inventing a test-count ratio **or** silently accepting incomplete coverage.

## Sources

- [CA-E-389-PROGRAMMATIC-GENERAL-EVAL_APPROACH--combine-complementary-software-behavior-evidence](../06_evaluation/CA-E-389-PROGRAMMATIC-GENERAL-EVAL_APPROACH--combine-complementary-software-behavior-evidence.md)
- [CA-E-536-PROGRAMMATIC-GENERAL-EVAL_APPROACH--admit-safe-canary-evaluation](../06_evaluation/CA-E-536-PROGRAMMATIC-GENERAL-EVAL_APPROACH--admit-safe-canary-evaluation.md)
- [CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)

- [CA-E-637 — Require observable evidence for behavioral acceptance](../06_evaluation/CA-E-637-PROGRAMMATIC-CORE-EVAL_APPROACH--require-observable-evidence-for-behavioral-acceptance.md)
- [CA-E-638 — Bound and recover canary exposure](../06_evaluation/CA-E-638-PROGRAMMATIC-CORE-EVAL_APPROACH--bound-and-recover-canary-exposure.md)
