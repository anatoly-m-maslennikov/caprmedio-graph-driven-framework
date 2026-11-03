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
# model
(Node, Node.**) {:0}((*));

Node {:0}((IS_PROPERTY_OF));

(Node, Node.**) {:0..1}((IS_PROPERTY_OF));

Node {:0+}((NARROWER_THAN)) Node;

Node {:0+}((HAS_NARROWER)) Node;

(Node, Node.**) {:0+}((HAS_PROPERTY)) Node.**;

IF $model_node in (Node, Node.**) THEN (
IF ($model_node {=0}((IS_PROPERTY_OF)))
THEN ($model_node >| (Independence == Primary Node));
);

IF $model_node_2 in (Node, Node.**) THEN (
IF ($model_node_2 {=1}((IS_PROPERTY_OF)))
THEN ($model_node_2 >| (Independence == Property))
AND ($model_node_2 {==0}((HAS_NARROWER)))
AND ($model_node_2 {==0}((HAS_INSTANCE)));
);

# instances
Node//$node;

($node, $node.**) {:0}((*));

$node {:0+}((INSTANCE_OF)) Node;

Node {:0+}((HAS_INSTANCE)) $node;

$node.** {:1}((IS_PROPERTY_OF)) ($node, $node.**);

($node, $node.**) {:0+}((HAS_PROPERTY)) $node.**;
```

## Semantics

A Node can be the Host or Target of a Relation.
