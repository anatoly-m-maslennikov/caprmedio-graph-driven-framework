---
atom_id: CA-R-1954
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/Directory.Path
relations:
  child_of:
  - CA-R-1174
version: 12
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1954-CORE_META_MODEL-DEFINITION--define-directory-carrier-path.md
  source_atom_id: CA-R-1954
  source_atom_revision: 12
  source_sha256: fd39775a7d05ecb3d134120798660c4f73625daaa9482bac038e31d0e418f6cf
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
## Summary

Define Directory Carrier.Path

## Claim scope

Directory Carrier filesystem locators.

## Claim

A Directory Carrier's Path **means** the locator of its directory within a filesystem, absolute or relative to a stated base. It does **not** define Scope Unit parentage or Carrier identity.

### Formal claim

```text
Directory.Path[string]{1}
```

## Details

CA-D-445 separates physical layout from declared hierarchy; CA-R-1660 says physical containment must not silently replace logical parentage. The Operator distinguishes Carrier ID from path.

Active CA-R-2515 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
