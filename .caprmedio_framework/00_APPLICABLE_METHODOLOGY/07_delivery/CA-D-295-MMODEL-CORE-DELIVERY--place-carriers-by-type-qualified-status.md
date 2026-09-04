---
atom_id: CA-D-295
cce_version: cce_1
cce_form: placement
subjects:
  governs:
    continuant:
      - Artifact/Carrier Placement
  depends_on:
    continuant:
      - Artifact/Activity
      - Entity/Type/Status
version: 4
updated_at: 2026-09-04 03:36:02 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-295-MMODEL-CORE-DELIVERY--place-carriers-by-type-qualified-status.md
---
# Place Carriers by Type-Qualified Status

an Artifact Carrier **must** live directly **in** its canonical current directory **if** Artifact Activity **`=`** Active **and** **otherwise** **must** live **in** the lowercase subdirectory named for its current type-qualified Status.
