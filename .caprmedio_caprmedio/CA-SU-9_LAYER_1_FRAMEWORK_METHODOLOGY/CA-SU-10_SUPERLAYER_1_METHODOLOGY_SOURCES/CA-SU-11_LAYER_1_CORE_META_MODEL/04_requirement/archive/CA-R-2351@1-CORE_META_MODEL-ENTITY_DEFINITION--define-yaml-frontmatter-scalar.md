---
atom_id: CA-R-2351@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Carrier/File.YAML Frontmatter.Scalar
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define YAML Frontmatter Scalar

## Claim scope

Direct primitive values within declared YAML Frontmatter metadata fields.

## Claim

A YAML Frontmatter Scalar is one direct primitive value within a declared metadata field of a File Carrier YAML Frontmatter; zero or more may occur. Registered YAML-safe controlled strings are serialized as plain scalars.

### Formal claim

```text
Entity/Carrier/File.YAML Frontmatter.Scalar[scalar]{0+}
```

## Details

Source meaning: CA-R-2269, CA-D-277. Scope-specific constraints remain in their governing Rs.
