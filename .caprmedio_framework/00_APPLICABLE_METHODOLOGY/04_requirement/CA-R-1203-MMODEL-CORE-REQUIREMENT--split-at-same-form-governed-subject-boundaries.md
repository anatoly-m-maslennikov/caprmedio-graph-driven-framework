---
atom_id: CA-R-1203
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - Atom/Claim
    occurrent:
      - Atom Splitting
  depends_on:
    continuant:
      - "Claim-Subject Relation/Kind: GOVERNS"
      - Claim-Subject Relation/Temporal Form
version: 2
updated_at: 2026-08-28 22:31:24 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1203-MMODEL-CORE-REQUIREMENT--split-at-same-form-governed-subject-boundaries.md
---
# Split at Same-Form Governed-Subject Boundaries

an Atom **must** be split **if** its Claim requires more than one independently replaceable GOVERNS Claim-Subject Relation with the same Temporal Form.
