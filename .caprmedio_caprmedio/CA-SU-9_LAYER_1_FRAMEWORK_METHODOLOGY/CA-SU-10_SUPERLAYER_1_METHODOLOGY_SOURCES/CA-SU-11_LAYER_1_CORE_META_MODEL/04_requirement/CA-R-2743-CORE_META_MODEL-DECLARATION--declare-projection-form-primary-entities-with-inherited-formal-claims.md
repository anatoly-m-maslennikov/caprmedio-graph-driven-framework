---
atom_id: CA-R-2743
ref_id: CA-R-2743
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form := Primary Entities with Inherited
    Formal Claims)
tier: 3
status: active
version: 3
updated_at: 2026-11-11 14:06:22 +0400
carrier_destination:
  file:
    name: CA-R-2743-CORE_META_MODEL-DECLARATION--declare-projection-form-primary-entities-with-inherited-formal-claims.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Projection/(.Form := Primary Entities with Inherited Formal Claims)

## Claim

### Prose Claim

For each Model Entity, group its Property and Relation rules by origin.

- Declared here. The Entity supplies the rule.
- Inherited. A broader Entity supplies the applicable rule.
- Overridden here. The Entity supplies a rule for the same Property or Relation as a broader Entity. Show both rules and their Declaration references.

Distinguish Direct and Derived Relations independently of rule origin. A derived inverse shows the same fact in reverse and retains its Direct Relation and source reference.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Projection


class PrimaryEntitiesWithInheritedFormalClaims(Projection):
    pass


declare_entity(
    entity_class=PrimaryEntitiesWithInheritedFormalClaims,
    entity_name="Primary Entities with Inherited Formal Claims",
    qualification_property_path="Projection.Form",
)
```
