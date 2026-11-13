---
atom_id: CA-R-1957
ref_id: CA-R-1957
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
tier: 3
relations:
  child_of:
  - CA-R-1174
status: active
version: 14
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-1957-CORE_META_MODEL-DECLARATION--define-entity-carrier-file-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Entity/Carrier/File Carrier

## Claim

### Prose Claim

A File Carrier represents content in a file.
### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Carrier

class File(Carrier):
    pass

declare_entity(entity_class=File, entity_name='File')
```

