---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
version: 18
updated_at: 2026-10-27 19:59:56 +0400
relations: {}
atom_id: CA-R-1503
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Keep Evaluation Atoms mechanism-neutral

## Scope

Evaluation Atom check definitions and their implementation mechanisms.

## Claim

an Evaluation Atom **must** define the checked Claim, applicable conditions, acceptance criteria, **and** disposition rule **without** prescribing the mechanism that realizes its check.

## Details

automated tests, model-judged evaluations, statistical assessments, rubrics, manual reviews, **and** other implementation mechanisms **may** realize that check. choosing a mechanism does **not** change the governing Evaluation Atom's Claim.
