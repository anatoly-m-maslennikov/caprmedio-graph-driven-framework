---
atom_id: CA-R-2003
content_role: Requirement
type: Graph Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Relation/Type: IS_BORNE_BY'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Dependent Entity Occurrences
relations: {}
version: 10
updated_at: 2026-10-27 20:00:07 +0400
tier: 1
claim:
  graph_rule_type: cardinality
  applies_to:
    node: Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Dependent Entity Occurrences
    relation_type: IS_BORNE_BY
    direction: outgoing
  condition:
    other_endpoint:
    - Subject/CAPRMEDIO/Graph/Node
    minimum: 1
    maximum: 1
---
# Summary

Require exactly one immediate bearer for each dependent Entity occurrence
