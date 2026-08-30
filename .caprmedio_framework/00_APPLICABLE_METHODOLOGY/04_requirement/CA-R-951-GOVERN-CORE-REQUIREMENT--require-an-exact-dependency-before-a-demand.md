---
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Requirement/Type: Demand/Admission"
  depends_on:
    continuant:
      - Consumer/Job
      - Producer/Result
atom_id: CA-R-951
cce_version: cce_1
cce_form: obligation
version: 8
updated_at: 2026-08-29 04:33:13 +0400
relations:
  child_of:
    - CA-R-933
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-951-GOVERN-CORE-REQUIREMENT--require-an-exact-dependency-before-a-demand.md
---
# Require an exact dependency before a Demand

a Consumer Scope Unit **must** own a Demand Atom **only** **when** its accepted Job authorizes an exact dependency on the demanded Producer result.
