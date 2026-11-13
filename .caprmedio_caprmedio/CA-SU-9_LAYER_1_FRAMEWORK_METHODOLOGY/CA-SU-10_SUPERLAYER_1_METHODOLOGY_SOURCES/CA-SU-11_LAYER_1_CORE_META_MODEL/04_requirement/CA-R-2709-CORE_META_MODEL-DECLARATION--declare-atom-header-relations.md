---
identity:
  atom_id: CA-R-2709
  ref_id: CA-R-2709
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Relations
  tier: 3
state:
  status: active
  version: 6
  updated_at: '2026-11-13T00:59:59.530485+00:00'
destination:
  file:
    name: CA-R-2709-CORE_META_MODEL-DECLARATION--declare-atom-header-relations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header.Relations

## Claim

### Prose Claim

Each child name is the canonical name of a declared Relation, and each child has one or more base Atom ID values. A present Relations group has at least one child.

The replacement Atom stores IS_REPLACEMENT_FOR with its predecessor Atom IDs.

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name="Relations",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Header",
    property_occurrence_cardinality=Cardinality(minimum=0, maximum=1),
    value_cardinality=0,
    dependent_property_cardinality=Cardinality(minimum=1, maximum=None),
    dependent_property_name_format=str,
    dependent_property_value_format=str,
    dependent_property_value_cardinality=Cardinality(minimum=1, maximum=None),
)
```
