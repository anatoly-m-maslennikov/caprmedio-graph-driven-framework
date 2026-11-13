---
atom_id: CA-R-2547
ref_id: CA-R-2547@4
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format//markdown
tier: 3
status: archived
version: 4
updated_at: 2026-11-11 16:04:42 +0400
carrier_destination:
  file:
    name: CA-R-2547@4-CORE_META_MODEL-ENTITY_DEFINITION--define-markdown-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define markdown value Format

## Claim

### Prose Claim


The markdown Format admits Markdown source. A section value preserves its markup. Its retrieved value includes its heading and descendant sections.

### Formal Claim

```CFEL
# model
Format//markdown ((INSTANCE_OF)) Format;
```
