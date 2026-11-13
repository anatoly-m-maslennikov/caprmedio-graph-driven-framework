---
atom_id: CA-R-2746
ref_id: CA-R-2746
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form := Entity Definition and Active
    Subject Coverage)
tier: 3
status: active
version: 3
updated_at: '2026-11-12T18:49:35.824257+00:00'
carrier_destination:
  file:
    name: CA-R-2746-CORE_META_MODEL-DECLARATION--declare-projection-form-entity-definition-and-active-subject-coverage.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Projection/(.Form := Entity Definition and Active Subject Coverage)

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Projection

class EntityDefinitionAndActiveSubjectCoverage(Projection):
    pass

declare_entity(entity_class=EntityDefinitionAndActiveSubjectCoverage, entity_name='Entity Definition and Active Subject Coverage', qualification_property_path="Projection.Form")
```
