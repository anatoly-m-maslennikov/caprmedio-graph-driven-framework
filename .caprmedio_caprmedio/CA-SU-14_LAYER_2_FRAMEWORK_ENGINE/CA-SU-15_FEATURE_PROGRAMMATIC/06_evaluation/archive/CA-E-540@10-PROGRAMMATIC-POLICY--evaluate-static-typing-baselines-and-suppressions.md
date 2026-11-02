---
atom_id: CA-E-540@10
content_role: Evaluation
type: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Source Check Adoption
  depends_on:
  - Subject/Graph Node/Engineering/Python Type Checks
relations:
  evaluation_for:
  - CA-M-420
  - CA-M-427
tier: 5
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
