---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Projection
  depends_on: []
version: 15
updated_at: 2026-10-25 17:32:27 +0400
relations:
  child_of:
  - CA-R-1746
atom_id: CA-R-1494
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary
Record Projection dependency provenance **only** **when** required

## Scope
Projections.

## Claim
a Projection **must** record dependency provenance **only** **when** its registered job requires that information; no Projection is required **to** persist a blanket source frontier.

this conditional recording obligation does **not** remove source traceability required by `CA-R-1746-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form` **or** a more specific admitted Projection specification.

## Details
