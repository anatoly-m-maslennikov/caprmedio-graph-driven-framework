---
atom_id: CA-R-1014
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - Atom/Current Scope/Governed Subject Set
  depends_on:
    continuant:
      - Subject
      - Atom/Current Scope/Owner
      - Atom/Claim Scope
      - Claim-Subject Relation/Kind: GOVERNS
version: 6
updated_at: 2026-09-02 00:35:23 +0400
relations:
  child_of:
    - CA-R-919
    - CA-R-1013
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1014-MMODEL-CORE-REQUIREMENT--limit-subject-derived-scope-coordinates.md
---
# Limit Subject-derived Scope Coordinates

an Atom's GOVERNS Subjects **must** determine **only** its Governed Subject Set **and** **must not** determine its Current Scope Owner **or** Claim Scope.
