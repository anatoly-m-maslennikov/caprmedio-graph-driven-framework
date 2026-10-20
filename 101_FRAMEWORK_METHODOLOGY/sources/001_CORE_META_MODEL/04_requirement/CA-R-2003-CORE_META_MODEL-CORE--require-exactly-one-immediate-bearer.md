---
atom_id: CA-R-2003
content_role: Requirement
type: Graph Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Relation/Type: IS_BORNE_BY'
  depends_on:
  - Entity
  - Entity/Node/Continuant/Selection//Dependent Entity Occurrences
relations: {}
version: 1
updated_at: "2026-10-20 13:37:52 +0400"
---
# Summary

Require exactly one immediate bearer for each dependent Entity occurrence

```yaml
graph_rule_type: cardinality
applies_to:
  node: "Entity/Node/Continuant/Selection//Dependent Entity Occurrences"
  relation_type: IS_BORNE_BY
  direction: outgoing
condition:
  other_endpoint:
    - Entity
  minimum: 1
  maximum: 1
```
