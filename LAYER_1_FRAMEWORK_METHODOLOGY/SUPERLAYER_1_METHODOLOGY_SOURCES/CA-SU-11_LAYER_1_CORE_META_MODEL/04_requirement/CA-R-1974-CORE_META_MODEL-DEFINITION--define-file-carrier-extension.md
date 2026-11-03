---
atom_id: CA-R-1974
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Carrier/File.Extension
relations:
  child_of:
  - CA-R-1174
version: 12
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Entity Definition
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
