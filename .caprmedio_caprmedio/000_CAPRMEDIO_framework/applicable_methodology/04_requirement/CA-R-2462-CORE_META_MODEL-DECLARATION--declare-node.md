---
atom_id: CA-R-2462
ref_id: CA-R-2462
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Node
tier: 3
status: Active
version: 6
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2462-CORE_META_MODEL-DECLARATION--declare-node.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2462-CORE_META_MODEL-DECLARATION--declare-node.md
  source_atom_id: CA-R-2462
  source_atom_revision: 6
  source_sha256: 725a3a66f857394014fa7c77fe734d6725eeb69455d5b9ad8655b8c0e28b49ec
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Node

## Claim

### Prose Claim

In the selected effective MODEL, each logical model entity selected by Node or Node.** has exactly one outgoing IS_DECLARED_BY Relation to its qualified canonical declaring Requirement/Form Declaration Atom. This named outgoing permission applies to model entities, including Node Properties, and does not impose an ownership requirement on runtime instances. Derive the view only from a GOVERNS fact satisfying the declaring ownership qualification; do not store a second fact or infer any other inverse permission. The target-omitted bound counts each selected model entity’s outgoing links within the Relation Declaration’s qualified endpoint domain.

### Formal Claim

```CFEL
# model
(Node, Node.**) {::0}((*));

Node {::0}((IS_PROPERTY_OF));

(Node, Node.**) {::0..1}((IS_PROPERTY_OF));

(Node, Node.**) {::1}((IS_DECLARED_BY));

Node {::0+}((NARROWER_THAN)) Node;

Node {::0+}((HAS_NARROWER)) Node;

Node.** {::1}((IS_PROPERTY_OF)) (Node, Node.**);

Atom.Header.** {::0..1}((IS_ORDERED_RIGHT_AFTER)) Atom.Header.**;

Atom.Header.** {::0..1}((IS_ORDERED_RIGHT_BEFORE)) Atom.Header.**;

Atom.Content.** {::0..1}((IS_ORDERED_RIGHT_AFTER)) Atom.Content.**;

Atom.Content.** {::0..1}((IS_ORDERED_RIGHT_BEFORE)) Atom.Content.**;

(Node, Node.**) {::0+}((HAS_PROPERTY)) Node.**;

Node.** {::0+}((HAS_INSTANCE)) Node.**//;

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
Node//$node;

($node, $node.**) {::0}((*));

$node {::0+}((INSTANCE_OF)) Node;

Node {::0+}((HAS_INSTANCE)) $node;

$node.** {::1}((IS_PROPERTY_OF)) ($node, $node.**);

$node.** {::1}((INSTANCE_OF)) Node.**;

Node.**//{::0..1};

($node, $node.**) {::0+}((HAS_PROPERTY)) $node.**;
```

## Semantics

A Node can be the Host or Target of a Relation.
