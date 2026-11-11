---
atom_id: CA-R-2351
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File.YAML Frontmatter.Scalar
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2351-CORE_META_MODEL-ENTITY_DEFINITION--define-yaml-frontmatter-scalar.md
  source_atom_id: CA-R-2351
  source_atom_revision: 2
  source_sha256: 4aa929f16c40799e90a2d82e299fc2683dc22616bdefde7bd5e9cefad7723ffd
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define YAML Frontmatter Scalar

## Claim scope

Direct primitive values within declared YAML Frontmatter metadata fields.

## Claim

A YAML Frontmatter Scalar is one direct primitive value within a declared metadata field of a File Carrier YAML Frontmatter; zero or more may occur. Registered YAML-safe controlled strings are serialized as plain scalars.

### Formal claim

```text
Carrier/File.YAML Frontmatter.Scalar[scalar]{0+}
```

## Details

Source meaning: CA-R-2269, CA-D-277. Scope-specific constraints remain in their governing Rs.
