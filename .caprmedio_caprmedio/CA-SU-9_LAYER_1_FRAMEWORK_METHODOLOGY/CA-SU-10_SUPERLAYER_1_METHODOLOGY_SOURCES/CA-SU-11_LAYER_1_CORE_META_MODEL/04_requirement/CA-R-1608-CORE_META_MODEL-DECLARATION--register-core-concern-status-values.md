---
atom_id: CA-R-1608
ref_id: CA-R-1608
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern).Header.State.Status
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
tier: 2
status: active
version: 24
updated_at: '2026-11-12T19:34:36.593311+00:00'
carrier_destination:
  file:
    name: CA-R-1608-CORE_META_MODEL-DECLARATION--register-core-concern-status-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register Core Concern Status Values

## Claim

### Prose Claim


the Core Concern Status model.


the Core Concern Status model **must** inherit the allowed values of Atom.Header.Status and add (Resolved, Canceled).

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Concern

declare_entity(
    entity_name='Status',
    relation_name="IS_PROPERTY_OF",
    base_path='Atom.Header.State',
    allowed_values=('Resolved', 'Canceled'),
    status_order_numbers={'Resolved': 21},
    applies_to_entity_classes=(Concern,),
)
```
