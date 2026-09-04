---
atom_id: CA-D-302
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - Atom/Scope/Filename Token
  depends_on:
    continuant:
      - Scope Unit/Name
      - Local Configuration
version: 4
updated_at: 2026-09-04 01:04:00 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-302-MMODEL-CORE-DELIVERY--serialize-scope-unit-references-as-filename-tokens.md
---
# Serialize Scope Unit References as Filename Tokens

**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Local Configuration.
