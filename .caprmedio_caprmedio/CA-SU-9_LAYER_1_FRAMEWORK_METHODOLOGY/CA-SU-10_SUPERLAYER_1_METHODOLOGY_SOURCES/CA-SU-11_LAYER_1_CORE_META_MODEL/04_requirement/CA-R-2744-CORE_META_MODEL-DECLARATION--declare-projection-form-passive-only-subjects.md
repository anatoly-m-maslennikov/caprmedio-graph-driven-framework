---
atom_id: CA-R-2744
ref_id: CA-R-2744
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form := Passive Only Subjects)
tier: 3
status: active
version: 3
updated_at: '2026-11-12T18:49:30.741730+00:00'
carrier_destination:
  file:
    name: CA-R-2744-CORE_META_MODEL-DECLARATION--declare-projection-form-passive-only-subjects.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Projection/(.Form := Passive Only Subjects)

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Projection

class PassiveOnlySubjects(Projection):
    pass

declare_entity(entity_class=PassiveOnlySubjects, entity_name='Passive Only Subjects', qualification_property_path="Projection.Form")
```
