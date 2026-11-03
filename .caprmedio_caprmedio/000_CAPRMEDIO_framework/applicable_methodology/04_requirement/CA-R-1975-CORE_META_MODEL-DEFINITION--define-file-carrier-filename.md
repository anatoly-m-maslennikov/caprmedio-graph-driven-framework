---
atom_id: CA-R-1975
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Carrier/File.Filename
relations:
  child_of:
  - CA-R-1174
version: 12
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1975-CORE_META_MODEL-DEFINITION--define-file-carrier-filename.md
  source_atom_id: CA-R-1975
  source_atom_revision: 12
  source_sha256: c4d4e950ea8d0f2c241fb000c95adaa52a740abb356ffcea0af2761c09054d8d
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
## Summary

Define File Carrier.Filename

## Claim scope

File Carrier names within their containing directories.

## Claim

A File Carrier's Filename **means** the name of its file within its containing directory, including any extension. It does **not** include the directory path.

### Formal claim

```text
File.Filename[string]{1}
```

## Details

CA-D-283 specifies filenames; CA-D-284 distinguishes filename tokens, Summary Slug and extension. Their concrete serialization patterns remain Delivery rules.

Active CA-R-2515 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
