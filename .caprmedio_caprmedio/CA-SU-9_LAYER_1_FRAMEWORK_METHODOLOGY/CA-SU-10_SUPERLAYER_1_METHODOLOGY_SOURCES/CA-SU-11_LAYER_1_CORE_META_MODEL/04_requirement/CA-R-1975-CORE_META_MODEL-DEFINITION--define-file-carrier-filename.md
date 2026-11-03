---
atom_id: CA-R-1975
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File.Filename
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

Define File Carrier.Filename

## Claim

### Prose Claim


File Carrier names within their containing directories.


A File Carrier's Filename **means** the name of its file within its containing directory, including any extension. It does **not** include the directory path.


```text
File.Filename[string]{1}
```

## Details

CA-D-283 specifies filenames; CA-D-284 distinguishes filename tokens, Summary Slug and extension. Their concrete serialization patterns remain Delivery rules.

Active CA-R-2515 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
