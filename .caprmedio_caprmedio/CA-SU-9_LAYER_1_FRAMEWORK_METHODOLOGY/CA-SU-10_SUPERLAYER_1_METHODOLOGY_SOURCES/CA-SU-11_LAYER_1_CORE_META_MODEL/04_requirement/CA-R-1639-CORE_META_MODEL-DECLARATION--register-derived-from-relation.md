---
atom_id: CA-R-1639
ref_id: CA-R-1639
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//DERIVED_FROM
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Artifact
tier: 1
status: active
version: 39
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-1639-CORE_META_MODEL-DECLARATION--register-derived-from-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register derived_from relation

## Claim

### Prose Claim

#### Applicability
direct derivation relations between exact represented content versions.

DERIVED_FROM means the directed Relation from a derived represented content version to an exact source content version used to derive it. Version references identify the relevant states; this does not introduce a Revision entity.

The Host is a derived represented-content version and the Target is the exact source content version used to derive it.
Forward `Host ((DERIVED_FROM)) Target` and reverse `Target <((DERIVED_FROM)) Host` are views of the same Relation fact.
DERIVED_FROM relates derived represented content version to exact source content version.
### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='DERIVED_FROM',
    source_endpoint={'level': 'instances', 'reference_form': 'represented_content_version'},
    target_endpoint={'level': 'instances', 'reference_form': 'exact_source_content_version'},
)
```

