---
atom_id: CA-D-264
cce_version: cce_1
cce_form: derivation
subjects:
  governs:
    continuant:
      - Structural Entity/Direct Containment
  depends_on:
    continuant:
      - Containment Relation Pair
      - Directory Carrier/Nesting
version: 6
updated_at: 2026-09-04 02:03:03 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-264-MMODEL-CORE-DELIVERY--derive-direct-containment-from-nearest-directory-carrier.md
---
# Derive Direct Containment from the Nearest Directory Carrier

an Artifact Revision whose canonical Carrier is nested below a Directory Carrier **must** derive one direct `CONTAINS` **and** `IS_CONTAINED_BY` relation pair with the Structural Entity Revision carried by its nearest ancestor Directory Carrier.
