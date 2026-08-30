---
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Requirement/Type: Demand/Producer Result"
  depends_on:
    continuant:
      - Consumer/Job
      - Producer/Result
atom_id: CA-R-933
cce_version: cce_1
cce_form: obligation
version: 8
updated_at: 2026-08-29 04:33:13 +0400
relations:
  child_of:
    - CA-R-932
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-933-MMODEL-CORE-REQUIREMENT--restrict-demand-to-one-depended-on-result.md
---
# Restrict Demand to one depended-on result

**every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Job depends.
