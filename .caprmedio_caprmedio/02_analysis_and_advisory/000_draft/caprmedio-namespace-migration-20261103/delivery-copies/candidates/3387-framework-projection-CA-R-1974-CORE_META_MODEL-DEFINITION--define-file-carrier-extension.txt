---
atom_id: CA-R-1974
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File.Extension
relations:
  child_of:
  - CA-R-1174
version: 12
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1974-CORE_META_MODEL-DEFINITION--define-file-carrier-extension.md
  source_atom_id: CA-R-1974
  source_atom_revision: 12
  source_sha256: 924b89dc6305129d2a9426b8d460b57ed5eb4d28caf92af1e7ff191f3a374327
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
## Summary

Define File Carrier.Extension

## Claim scope

File Carriers whose filename uses an extension.

## Claim

A File Carrier's Extension **means** the filename suffix used to indicate its format. The extension does **not** establish the carried Entity's identity.

### Formal claim

```text
File.Extension[string]{0..1}
```

## Details

CA-D-283 uses an extension segment; CA-D-284 constrains its case; CA-D-507 explicitly separates changes of extension from Entity identity. This draft does not require every file to have an extension.

Active CA-R-2515 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
