---
atom_id: CA-E-540
ref_id: CA-E-540
role: Evaluation
form: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 19:59:37 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis
relations:
  evaluation_for:
  - CA-M-420
  - CA-M-427
tier: 5
container:
  scope_unit: CA-SU-15
carrier_destination:
  file:
    name: CA-E-540-PROGRAMMATIC-POLICY--evaluate-static-typing-baselines-and-suppressions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
# Summary

Evaluate static typing baselines and suppressions

## Scope

new **or** materially changed hand-authored PROGRAMMATIC Python targets **in**
the admitted Mypy target set.

## Claim

given the pinned Mypy profile, bounded target set, current diagnostics, recorded
passing baseline, **and** suppression rationale, accept typing conformance
**only when** new targets pass the strict admitted profile; changed targets do
**not** regress below their passing baseline; **and** **every** suppression has an
explanation at the narrowest affected line **or** symbol. reject regression **or**
an unexplained broad suppression. return unresolved **when** the profile, target
set, required baseline, **or** current evidence is unavailable.

## Details

static typing evidence remains distinct from runtime-validation **and** behavioral
evidence. unmodified legacy targets outside the admitted surface do **not** become
an unrelated whole-project blocker.

CA-M-427 owns Mypy selection **and** its implementation convention; CA-M-420 owns
bounded capability adoption. this Evaluation owns their typing acceptance policy.
