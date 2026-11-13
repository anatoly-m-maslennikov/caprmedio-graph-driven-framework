---
atom_id: CA-R-2734
ref_id: CA-R-2734
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Workflow/(.Purpose
    := Runtime)
tier: 3
status: active
version: 4
updated_at: '2026-11-13T03:39:08.573175+00:00'
container:
  scope_unit: CA-SU-11
destination:
  file:
    name: CA-R-2734-CORE_META_MODEL-DECLARATION--declare-runtime-workflow.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Runtime Workflow

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name="Purpose",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom/(.Header.Context.Role := Operations)/Workflow",
    allowed_values=('Runtime',),
)
```

## Semantics

A Runtime Workflow is a Workflow whose Purpose is Runtime: it provides behavior through a Project's delivered result during its operation. In CAPRMEDIO, examples include Create Draft, Promote Draft and Archive Atom.

It inherits Workflow's shared Step, Substep and Action model. Purpose describes use relative to a Project and does not change the canonical definition's owning Scope Unit.
