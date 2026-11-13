---
atom_id: CA-R-2765
ref_id: CA-R-2765
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Method)/(.Header.Context.Form
    := Term Definition)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Method)
tier: 3
status: active
version: 7
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2765-CORE_META_MODEL-DECLARATION--declare-term-definition-as-a-method-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Term Definition as a Method Form

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Method

class TermDefinition(Method):
    pass

declare_entity(entity_class=TermDefinition, entity_name='Term Definition', qualification_property_path="Atom.Header.Context.Form")
```
