---
atom_id: CA-R-1539
ref_id: CA-R-1539
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
tier: 2
status: active
version: 26
updated_at: '2026-11-12T21:16:58.190634+00:00'
carrier_destination:
  file:
    name: CA-R-1539-CORE_META_MODEL-DECLARATION--register-core-plan-status-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register Core Plan Status Values

## Claim

### Prose Claim


Core Plan Status values.


the Core Plan Status model **must** inherit the allowed values of Atom.Header.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.

### Formal Claim

```python
from caprmedio.model import Plan
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name="Status",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Header.State",
    applies_to_entity_classes=(Plan,),
    allowed_values=("Backlog", "Done", "Canceled"),
    status_order_numbers={"Backlog": 1, "Done": 20, "Canceled": 40},
    status_groups={"Backlog": "Backlog"},
)
```
