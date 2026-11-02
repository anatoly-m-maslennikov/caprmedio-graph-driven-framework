---
atom_id: CA-R-2003@11-draft
content_role: Requirement
type: Graph Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: 'Formal Model::CAPRMEDIO::Graph Relation/Type: IS_BORNE_BY'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Dependent Entity Occurrences
relations: {}
version: 11
updated_at: 2026-10-28 19:24:50 +0400
tier: 1
---
# Summary

Require exactly one immediate bearer for each dependent Entity occurrence

## Claim

```yaml
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
```

## Details

Superseded preparation: CA-A-1242 removes the special Graph Rule branch and Atom Type. Do not promote this legacy Graph Rule packet entry as written. Preserve its useful formal constraints/schema evidence for incorporation into the appropriate Definition Claims; no Current rule or predecessor is deleted by this marker.
