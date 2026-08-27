---
atom_id: CA-D-253
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - Applicable Methodology/Carrier
  depends_on:
    continuant:
      - Applicable Methodology
      - Applicable Methodology/Sources
version: 2
updated_at: 2026-08-27 20:40:00 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-253-GOVERN-DELIVERY--place-applicable-methodology-and-its-sources.md
---
# Place Applicable Methodology and Its Sources

the Delivery Authority **must** reserve `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/` for exactly three structural Source Layers in (CORE_META_MODEL, INSTALLED_EXTENSIONS, LOCAL_CONFIGURATION) and place every generated projected Atom Carrier at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/<04_requirement|05_method|06_evaluation|07_delivery|09_ops>/<source basename>`.
