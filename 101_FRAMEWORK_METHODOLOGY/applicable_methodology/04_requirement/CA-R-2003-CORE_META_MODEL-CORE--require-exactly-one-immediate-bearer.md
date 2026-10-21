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
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-2003-CORE_META_MODEL-CORE--require-exactly-one-immediate-bearer.md
  source_atom_id: CA-R-2003
  source_atom_revision: 1
  source_sha256: e5f0233d7b10da40900dd5aec1c609ac8e3a0c643782fb39087b4f36b2775637
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
