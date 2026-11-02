---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation/Type'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - Subject/Graph Node/Engineering/Evaluation Technique Selection
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation/Type'
version: 14
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1506@14
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Separate check mechanism labels from Evaluation Atom Types

## Scope

mechanism labels and admitted Type values for Evaluation Atoms.

## Claim

the mechanism labels `Test` **and** `Evaluation` **must** describe implementation mechanisms, **not** Type values under `Atom/Content Role: Evaluation/Type`. the governing Evaluation Atom **and** its realization **must not** acquire the same classification merely because their names overlap.

## Details

this distinction does **not** define another Content Role **or** close the admitted Evaluation Type domain. its separately governed Type values remain subject **to** the applicable Type authority.
