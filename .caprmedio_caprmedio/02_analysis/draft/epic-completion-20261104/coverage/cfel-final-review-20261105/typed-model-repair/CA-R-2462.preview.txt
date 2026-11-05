---
atom_id: CA-R-2462
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Node
version: 5
updated_at: 2026-11-05 16:33:24 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2462@5-draft-CORE_META_MODEL-DECLARATION--declare-node.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare Node

## Claim

### Formal Claim

```CFEL
# model
(Node, Node.**) {::0}((*));

(Node, Node.**) {::0+}((HAS_ALLOWED_VALUE));

(Node, Node.**) {::0+}((HAS_VALUE_CONSTRAINT));

Node {::0}((IS_PROPERTY_OF));

(Node, Node.**) {::0..1}((IS_PROPERTY_OF));

(Node, Node.**) {::1}((IS_DECLARED_BY));

Node {::0+}((NARROWER_THAN)) Node;

Node {::0+}((HAS_NARROWER)) Node;

Node.** {::1}((IS_PROPERTY_OF)) (Node, Node.**);

(Node, Node.**) {::0+}((HAS_PROPERTY)) Node.**;

Node.** {::0+}((HAS_INSTANCE));

IF $model_node in (Node, Node.**) THEN (
IF ($model_node {=0}((IS_PROPERTY_OF)))
THEN ($model_node >| (Independence == Primary Node));
);

IF $model_node_2 in (Node, Node.**) THEN (
IF ($model_node_2 {=1}((IS_PROPERTY_OF)))
THEN ($model_node_2 >| (Independence == Property))
AND ($model_node_2 {==0}((HAS_NARROWER)));
);

# instances
$node[<Node>];

($node, $node.**) {::0}((*));

($node, $node.**) {::0+}((HAS_ALLOWED_VALUE));

($node, $node.**) {::0+}((HAS_VALUE_CONSTRAINT));

$node {::0+}((INSTANCE_OF)) Node;

Node {::0+}((HAS_INSTANCE)) $node;

$node.** {::1}((IS_PROPERTY_OF)) ($node, $node.**);

$node.** {::1}((INSTANCE_OF)) Node.**;

($node, $node.**) {::0+}((HAS_PROPERTY)) $node.**;
```

### Prose Claim

In the selected effective MODEL, each logical model entity selected by Node or Node.** has exactly one outgoing IS_DECLARED_BY Relation to its qualified canonical declaring Requirement/Form Declaration Atom. This named outgoing permission applies to model entities, including Node Properties, and does not impose an ownership requirement on runtime instances. Derive the view only from a GOVERNS fact satisfying the declaring ownership qualification; do not store a second fact or infer any other inverse permission. The target-omitted bound counts each selected model entity’s outgoing links within the Relation Declaration’s qualified endpoint domain.

## Semantics

A Node can be the Host or Target of a Relation.
