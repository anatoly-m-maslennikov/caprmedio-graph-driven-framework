---
atom_id: CA-R-1950
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Carrier.Format
relations:
  child_of:
  - CA-R-1174
version: 12
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1950-CORE_META_MODEL-DEFINITION--define-carrier-format.md
  source_atom_id: CA-R-1950
  source_atom_revision: 12
  source_sha256: 16942383effb3d2c30b768f028a8330523130daec86e104452c50aafa725a81d
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
## Summary

Define Carrier.Format

## Claim scope

Carriers with an applicable representation format.

## Claim

A Carrier's Format **means** the rules for encoding and interpreting its represented content. The registered File Carrier values include Markdown, TOML, YAML and JSON under CA-D-262; representation details remain governed by Delivery.

### Formal claim

```text
Carrier/File.Format: Markdown
Carrier/File.Format: TOML
Carrier/File.Format: YAML
Carrier/File.Format: JSON
```

## Details

CA-D-262 admits registered File Carrier formats including Markdown, TOML, YAML and JSON; CA-D-507 distinguishes format from identity. This definition does not require a format value for every Directory Carrier.

