---
atom_id: CA-R-2247
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 11
updated_at: 2026-11-04 22:17:58 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2247-CORE_META_MODEL-ENTITY_DEFINITION--define-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2247-CORE_META_MODEL-ENTITY_DEFINITION--define-relation.md
  source_atom_id: CA-R-2247
  source_atom_revision: 11
  source_sha256: b2204c4e8d43421bc1fa95ebf93dfae03eaf6749cef10015f97d3563bdb8cc22
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Define Relation

## Claim

### Formal Claim

```CFEL
# model
Relation;

Relation.** {:1}((IS_PROPERTY_OF)) (Relation, Relation.**);
(Relation, Relation.**) {:0+}((HAS_PROPERTY)) Relation.**;

# instances
Relation//$relation;
$relation.** {:1}((IS_PROPERTY_OF)) ($relation, $relation.**);
($relation, $relation.**) {:0+}((HAS_PROPERTY)) $relation.**;
```

### Prose Claim

Relation defines a reusable directed graph Relation Type with a Name and Meaning. Each actual link is a tuple (Host, Relation Type, Target); persist each direct fact once. An actual edge does not create a separate Relation ID. Endpoints are declared model Entities or instances, including Carrier and CFEL descriptors, and exclude literal values and glyphs. An operator is distinct from a graph Relation even when its notation spells a Relation traversal. Its declared descriptor may be an endpoint.

A direct Relation Declaration owns shared meaning, endpoint signature and any counterpart binding. A derived counterpart remains a distinct Relation with its own Declaration; its meaning and endpoints are inferred through that binding. An alias supplies lexical notation for one Relation; it does not create a new Relation, a Node or a separate Relation ID.
