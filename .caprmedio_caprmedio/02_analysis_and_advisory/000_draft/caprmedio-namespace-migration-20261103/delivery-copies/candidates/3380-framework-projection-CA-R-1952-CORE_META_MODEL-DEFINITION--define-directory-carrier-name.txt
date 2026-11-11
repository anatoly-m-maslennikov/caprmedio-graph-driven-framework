---
atom_id: CA-R-1952
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/Directory.Name
relations:
  child_of:
  - CA-R-1174
version: 12
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1952-CORE_META_MODEL-DEFINITION--define-directory-carrier-name.md
  source_atom_id: CA-R-1952
  source_atom_revision: 12
  source_sha256: 81eeeb680e003318f2141cea5b1053d20e5d8f6864c6030de094eabff9831ad2
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
## Summary

Define Directory Carrier.Name

## Claim scope

Directory Carrier names within their parent directories.

## Claim

A Directory Carrier's Name **means** the name of its directory within its parent directory, excluding the parent path.

### Formal claim

```text
Directory.Name[string]{1}
```

## Details

CA-D-297 and CA-D-299 constrain authority and Delivery directory names. CA-D-445 permits explicit native layouts. The directory name is not universally identical to the carried Scope Unit's Name.

Active CA-R-2515 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
