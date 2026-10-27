---
subjects:
  governs: Subject/Graph/Rule
  depends_on:
  - Subject/Graph/Rule.Type
  - Subject/Graph/Rule.Applies To
  - Subject/Graph/Rule.Condition
  - Subject/Domain/Node/Continuant/Selection//Stored Governing RMED Relation Occurrences
  - Subject/Domain/Node/Continuant/Atom.Tier
  - Subject/Domain/Node/Continuant/Scope Unit
relations: {}
atom_id: CA-R-2149@5
content_role: Requirement
type: Graph Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 13:39:34 +0400
---
# Summary

Constrain Governing RMED Relation Targets by Numeric Tier and Scope Ancestry

```yaml
graph_rule_type: endpoint_constraint
applies_to:
  relation_selection: "Subject/Domain/Node/Continuant/Selection//Stored Governing RMED Relation Occurrences"
condition:
  ordering: same_scope_lower_target_tier_or_strict_ancestor
```

## Semantics

Ordering contexts follow CA-D-637. A verified Project Goal uses its Target Project, while its owner remains the Operator Actor; ordinary endpoints use their Local Scope Unit. The numeric comparison and strict-ancestor rule are unchanged.
