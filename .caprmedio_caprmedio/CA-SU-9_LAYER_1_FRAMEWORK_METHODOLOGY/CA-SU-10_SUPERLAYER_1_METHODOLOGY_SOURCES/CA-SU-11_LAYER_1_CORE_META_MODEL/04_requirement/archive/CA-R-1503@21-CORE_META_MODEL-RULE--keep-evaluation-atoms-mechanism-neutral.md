---
subjects:
  active: Atom/(.Role := Evaluation)
  passive:
  - Atom.Content
  - Entity/Aspect/Engineering/Verification
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1503@21
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 1
role: Requirement
form: Rule
---
## Summary

Keep Evaluation Atoms mechanism-neutral

## Claim scope

Evaluation Atom check definitions and their implementation mechanisms.

## Claim

an Evaluation Atom **must** define the checked Claim, applicable conditions, acceptance criteria, **and** disposition rule **without** prescribing the mechanism that realizes its check.

## Details

automated tests, model-judged evaluations, statistical assessments, rubrics, manual reviews, **and** other implementation mechanisms **may** realize that check. choosing a mechanism does **not** change the governing Evaluation Atom's Claim.
