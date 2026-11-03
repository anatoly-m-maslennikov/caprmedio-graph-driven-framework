---
atom_id: CA-R-2351
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File.YAML Frontmatter.Scalar
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Entity Definition
---
## Summary

Define YAML Frontmatter Scalar

## Claim

### Prose Claim


Direct primitive values within declared YAML Frontmatter metadata fields.


A YAML Frontmatter Scalar is one direct primitive value within a declared metadata field of a File Carrier YAML Frontmatter; zero or more may occur. Registered YAML-safe controlled strings are serialized as plain scalars.


```text
Carrier/File.YAML Frontmatter.Scalar[scalar]{0+}
```

## Details

Source meaning: CA-R-2269, CA-D-277. Scope-specific constraints remain in their governing Rs.
