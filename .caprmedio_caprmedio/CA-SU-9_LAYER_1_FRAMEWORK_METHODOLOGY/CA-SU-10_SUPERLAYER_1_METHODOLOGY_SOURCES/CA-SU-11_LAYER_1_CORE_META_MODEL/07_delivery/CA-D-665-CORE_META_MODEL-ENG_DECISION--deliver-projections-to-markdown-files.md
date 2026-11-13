---
atom_id: CA-D-665
ref_id: CA-D-665
container:
  scope_unit: CA-SU-11
role: Delivery
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 3
status: active
version: 3
updated_at: '2026-11-13T04:48:22.388242+00:00'
carrier_destination:
  file:
    name: CA-D-665-CORE_META_MODEL-ENG_DECISION--deliver-projections-to-markdown-files.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Deliver Projections to Markdown files

## Claim

### Formal Claim

```python
# instances
deliver(
    source="Projection//$projection",
    carrier="Carrier/File/Markdown//$carrier",
)
```
