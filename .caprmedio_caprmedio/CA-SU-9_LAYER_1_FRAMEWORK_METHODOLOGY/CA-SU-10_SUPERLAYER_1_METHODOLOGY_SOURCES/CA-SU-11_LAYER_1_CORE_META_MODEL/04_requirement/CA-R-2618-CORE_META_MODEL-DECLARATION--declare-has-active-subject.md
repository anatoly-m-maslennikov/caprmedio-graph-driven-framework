---
atom_id: CA-R-2618
ref_id: CA-R-2618
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_ACTIVE_SUBJECT
tier: 3
status: active
version: 4
updated_at: 2026-11-05 14:25:52 +0400
carrier_destination:
  file:
    name: CA-R-2618-CORE_META_MODEL-DECLARATION--declare-has-active-subject.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare HAS_ACTIVE_SUBJECT

## Claim

### Prose Claim

HAS_ACTIVE_SUBJECT links an Atom to the declared model entity or instance named by its active Subject. This includes a Requirement/Form Declaration's target and is not restricted to the Node branch. Carrier entities, CFEL operator descriptors, graph Relation types and their declared instances are admitted when selected by the active Subject. Literal values and operator glyphs are not endpoints.

The Host is an Atom and the Target is the entity or instance resolved from its dedicated active Subject field. The field's source supplies the canonical HAS_ACTIVE_SUBJECT fact; obtaining that value from the field does not make this Relation a derived view of another Relation. An unresolved Subject remains a diagnostic, not an empty or automatically valid target population.

Forward `Host ((HAS_ACTIVE_SUBJECT)) Target` and reverse `Target <((HAS_ACTIVE_SUBJECT)) Host` are written views of the same fact. Ownership cardinalities are supplied by their applicable rules; this endpoint signature does not itself create an ownership count.
### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='HAS_ACTIVE_SUBJECT',
    source_endpoint={'level': 'instances', 'entity_paths': ('Atom',)},
    target_endpoint={'level': 'model_entities_or_instances'},
)
```