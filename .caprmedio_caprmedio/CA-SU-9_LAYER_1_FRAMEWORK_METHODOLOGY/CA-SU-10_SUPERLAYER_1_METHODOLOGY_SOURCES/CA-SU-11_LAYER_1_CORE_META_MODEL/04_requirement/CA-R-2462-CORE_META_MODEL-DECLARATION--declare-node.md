---
atom_id: CA-R-2462
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Node
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Node

## Claim

### Formal Claim

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
