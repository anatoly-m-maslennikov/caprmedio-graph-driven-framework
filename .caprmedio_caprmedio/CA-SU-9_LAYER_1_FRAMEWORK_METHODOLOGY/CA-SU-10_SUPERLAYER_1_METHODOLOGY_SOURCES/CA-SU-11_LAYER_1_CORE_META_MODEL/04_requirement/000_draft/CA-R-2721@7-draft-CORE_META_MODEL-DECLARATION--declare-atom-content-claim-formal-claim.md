---
atom_id: CA-R-2721
ref_id: CA-R-2721@7-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Claim.Formal Claim
tier: 3
status: draft
version: 7
updated_at: '2026-11-13T14:59:14.324891+00:00'
carrier_destination:
  file:
    name: CA-R-2721@7-draft-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-formal-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Atom.Content.Claim.Formal Claim

## Claim

### Prose Claim

Formal Claim is a child Property of Claim. Its value contains one fenced formal expression. Use Python for the Formal Claim.
### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name="Formal Claim",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Content.Claim",
    applies_to_entity_classes=("Requirement", "Method", "Evaluation", "Delivery"),
    value_format="markdown",
    value_cardinality=Cardinality(minimum=0, maximum=1),
    dependent_property_cardinality=0,
)
```
