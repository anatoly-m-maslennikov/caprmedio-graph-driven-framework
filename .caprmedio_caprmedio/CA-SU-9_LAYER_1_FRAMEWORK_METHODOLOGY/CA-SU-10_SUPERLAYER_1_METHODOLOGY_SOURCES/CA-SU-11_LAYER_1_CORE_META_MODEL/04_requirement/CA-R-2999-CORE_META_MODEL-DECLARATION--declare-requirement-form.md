---
atom_id: CA-R-2999
ref_id: CA-R-2999
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form
    := Requirement)
tier: 3
status: active
version: 4
updated_at: '2026-11-13T04:57:09.691167+00:00'
carrier_destination:
  file:
    name: CA-R-2999-CORE_META_MODEL-DECLARATION--declare-requirement-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Requirement Form

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Requirement


class RequirementForm(Requirement):
    pass


declare_entity(
    entity_name="Requirement",
    entity_class=RequirementForm,
    qualification_property_path="Atom.Header.Context.Form",
)
```

## Semantics

A Requirement Form states a local required outcome, behavior, property or constraint.
