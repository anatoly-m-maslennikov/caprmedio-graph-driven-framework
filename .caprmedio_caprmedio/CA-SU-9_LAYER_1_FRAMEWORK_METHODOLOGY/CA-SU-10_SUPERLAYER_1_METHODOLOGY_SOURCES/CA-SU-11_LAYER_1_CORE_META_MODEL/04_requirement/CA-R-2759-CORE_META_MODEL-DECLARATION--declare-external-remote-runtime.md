---
atom_id: CA-R-2759
ref_id: CA-R-2759
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ External Remote Runtime
tier: 3
status: active
version: 1
updated_at: 2026-11-04 16:07:35 +0400
carrier_destination:
  file:
    name: CA-R-2759-CORE_META_MODEL-DECLARATION--declare-external-remote-runtime.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare External Remote Runtime

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Runtime

class ExternalRemoteRuntime(Runtime):
    pass

declare_entity(
    entity_class=ExternalRemoteRuntime,
    entity_name='External Remote Runtime',
)
```

## Semantics

An External Remote Runtime is a Runtime external to our application on a machine other than the Operator’s.
