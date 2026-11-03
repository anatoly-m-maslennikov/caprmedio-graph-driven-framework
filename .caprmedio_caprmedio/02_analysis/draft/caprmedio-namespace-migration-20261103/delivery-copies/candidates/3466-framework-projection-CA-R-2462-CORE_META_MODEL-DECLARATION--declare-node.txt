---
atom_id: CA-R-2462
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Node
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2462-CORE_META_MODEL-DECLARATION--declare-node.md
  source_atom_id: CA-R-2462
  source_atom_revision: 2
  source_sha256: 8a4306294502ad99f9f6e00668c40bdbe0ed1946fc058681be05ae51a946ed14
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Node

## Claim

```CFEL
(Node, Node.**) {:0}((*));
(Node//, (Node//).**) {:0}((*));
Node {:0}((IS_PROPERTY_OF));
(Node, Node.**) {:0..1}((IS_PROPERTY_OF));
Node {:0+}((NARROWER_THAN)) Node;
Node {:0+}((HAS_NARROWER)) Node;
(Node, Node.**) {:0+}((HAS_PROPERTY)) Node.**;
Node// {:0+}((INSTANCE_OF)) Node;
Node {:0+}((HAS_INSTANCE)) Node//;
(Node//).** {:1}((IS_PROPERTY_OF)) (Node//, (Node//).**);
(Node//, (Node//).**) {:0+}((HAS_PROPERTY)) (Node//).**;
IF ((Node, Node.**) {=0}((IS_PROPERTY_OF)))
THEN ((Node, Node.**) >| (Independence == Primary Node));
IF ((Node, Node.**) {=1}((IS_PROPERTY_OF)))
THEN ((Node, Node.**) >| (Independence == Property))
AND ((Node, Node.**) {==0}((HAS_NARROWER)))
AND ((Node, Node.**) {==0}((HAS_INSTANCE)))
```

## Semantics

A Node can be the Host or Target of a Relation.
