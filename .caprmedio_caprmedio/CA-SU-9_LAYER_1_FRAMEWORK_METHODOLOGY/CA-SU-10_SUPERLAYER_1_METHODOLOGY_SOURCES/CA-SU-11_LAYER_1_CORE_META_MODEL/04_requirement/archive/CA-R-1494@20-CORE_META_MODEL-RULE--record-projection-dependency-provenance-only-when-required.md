---
subjects:
  active: Projection
  passive: []
version: 20
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2535
atom_id: CA-R-1494@20
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 2
role: Requirement
form: Rule
---
## Summary
Record Projection dependency provenance **only** **when** required

## Claim scope
Projections.

## Claim
a Projection **must** record dependency provenance **only** **when** its registered job requires that information; no Projection is required **to** persist a blanket source frontier.

this conditional recording obligation does **not** remove source traceability required by `CA-R-2535-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form` **or** a more specific admitted Projection specification.
