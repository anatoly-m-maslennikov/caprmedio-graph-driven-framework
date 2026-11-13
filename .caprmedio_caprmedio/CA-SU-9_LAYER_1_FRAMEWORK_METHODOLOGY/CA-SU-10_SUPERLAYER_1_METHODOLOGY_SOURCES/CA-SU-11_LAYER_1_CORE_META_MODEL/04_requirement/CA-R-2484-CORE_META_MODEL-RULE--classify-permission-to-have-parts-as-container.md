---
atom_id: CA-R-2484
ref_id: CA-R-2484
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Node >| Container
tier: 3
status: active
version: 3
updated_at: '2026-11-13T03:23:30.209307+00:00'
carrier_destination:
  file:
    name: CA-R-2484-CORE_META_MODEL-RULE--classify-permission-to-have-parts-as-container.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Classify permission to have parts as Container

## Claim

### Prose Claim


Container is a classification whose admitted value cases are yes and no:


The yes case permits the Node to be the whole endpoint of CONTAINS, subject to its effective Relation whitelist and cardinalities. It does not by itself require a part. The no case forbids that endpoint role. Whether a part may belong to a whole is distinct from whether that part may itself have parts.

Use `Node// >| Container = yes` when selecting eligible whole instances. Container is not a required Boolean Property authored on every instance. This Draft does not assign an implicit default or require a classification annotation for every Node.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name="Node",
    allowed_classification_values={"Container": ("yes", "no")},
)
```

## Details

The Operator chose IS_CONTAINED_BY / CONTAINS and Container: yes/no. Current CA-R-1945@13 distinguishes permission from a requirement to have children; retain that distinction while replacing the old Atom.Enabled Relations.Contains Property representation. Its default-False mechanism is not silently imported into the new general classification. Explicit CONTAINS cardinalities can require parts for a particular Node, such as Workflow.
