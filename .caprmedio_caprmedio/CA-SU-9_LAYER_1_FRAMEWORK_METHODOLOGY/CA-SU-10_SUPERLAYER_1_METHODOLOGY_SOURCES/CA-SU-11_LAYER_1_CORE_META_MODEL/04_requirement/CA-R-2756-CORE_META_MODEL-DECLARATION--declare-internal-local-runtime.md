---
atom_id: CA-R-2756
ref_id: CA-R-2756
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Internal Local Runtime
tier: 3
status: active
version: 1
updated_at: 2026-11-04 16:07:35 +0400
carrier_destination:
  file:
    name: CA-R-2756-CORE_META_MODEL-DECLARATION--declare-internal-local-runtime.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Internal Local Runtime

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Runtime

class InternalLocalRuntime(Runtime):
    pass

declare_entity(
    entity_class=InternalLocalRuntime,
    entity_name='Internal Local Runtime',
)
```

## Semantics

An Internal Local Runtime is a Runtime of our application on the Operator’s machine.
