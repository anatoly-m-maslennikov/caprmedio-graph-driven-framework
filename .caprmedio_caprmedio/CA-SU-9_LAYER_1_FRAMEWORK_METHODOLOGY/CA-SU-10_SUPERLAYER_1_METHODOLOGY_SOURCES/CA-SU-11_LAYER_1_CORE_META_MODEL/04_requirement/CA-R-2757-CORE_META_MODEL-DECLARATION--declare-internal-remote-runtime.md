---
atom_id: CA-R-2757
ref_id: CA-R-2757
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Internal Remote Runtime
tier: 3
status: active
version: 1
updated_at: 2026-11-04 16:07:35 +0400
carrier_destination:
  file:
    name: CA-R-2757-CORE_META_MODEL-DECLARATION--declare-internal-remote-runtime.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Internal Remote Runtime

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Runtime

class InternalRemoteRuntime(Runtime):
    pass

declare_entity(
    entity_class=InternalRemoteRuntime,
    entity_name='Internal Remote Runtime',
)
```

## Semantics

An Internal Remote Runtime is a Runtime of our application on a machine other than the Operator’s.
