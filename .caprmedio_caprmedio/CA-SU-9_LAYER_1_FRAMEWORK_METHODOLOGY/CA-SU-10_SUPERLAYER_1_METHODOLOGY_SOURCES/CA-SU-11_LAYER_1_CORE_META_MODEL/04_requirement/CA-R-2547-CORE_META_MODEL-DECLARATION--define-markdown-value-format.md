---
atom_id: CA-R-2547
ref_id: CA-R-2547
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format//markdown
tier: 3
status: active
version: 5
updated_at: '2026-11-13T05:17:03.034051+00:00'
carrier_destination:
  file:
    name: CA-R-2547-CORE_META_MODEL-DECLARATION--define-markdown-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define markdown value Format

## Claim

### Prose Claim


The markdown Format admits Markdown source. A section value preserves its markup. Its retrieved value includes its heading and descendant sections.

### Formal Claim

```python
# model
relation(source='Format//markdown', name='INSTANCE_OF', target='Format')
```
