---
atom_id: CA-R-2485
ref_id: CA-R-2485
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_INVERSE
tier: 3
status: active
version: 9
updated_at: '2026-11-13T00:36:29.288696+00:00'
carrier_destination:
  file:
    name: CA-R-2485-CORE_META_MODEL-DECLARATION--define-has-inverse.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define HAS_INVERSE

## Claim

### Prose Claim

HAS_INVERSE binds a canonical Relation to its reverse alias. The canonical Declaration defines the shared meaning, endpoint constraints, and alias. The reverse view follows from the same graph fact. It swaps the endpoints and their cardinality slots and retains any declared qualification.

`<-->` writes this binding in a Subject. `Relation//DIRECT <--> Relation//REVERSE` names the canonical Relation on the left and its reverse alias on the right. Each direction keeps its own admitted permissions and bounds.

### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='HAS_INVERSE',
    source_endpoint={'level': 'model_entities', 'entity_paths': ('Relation',), 'address_form': 'canonical'},
    target_endpoint={'level': 'model_entities', 'entity_paths': ('Relation',), 'address_form': 'inverse_alias'},
    written_alias='<-->',
)
```
