---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Rule
  depends_on:
  - Subject/CAPRMEDIO/Graph/Rule.Type
  - Subject/CAPRMEDIO/Graph/Rule.Applies To
  - Subject/CAPRMEDIO/Graph/Rule.Condition
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Stored Governing RMED Relation Occurrences
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
relations: {}
atom_id: CA-R-2149
content_role: Requirement
type: Graph Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 20:00:08 +0400
claim:
  graph_rule_type: endpoint_constraint
  applies_to:
    relation_selection: Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Stored Governing RMED Relation Occurrences
  condition:
    ordering: same_scope_lower_target_tier_or_strict_ancestor_or_project_configuration_core_prerequisite
---
# Summary

Constrain Governing RMED Relation Targets by Numeric Tier and Scope Ancestry

## Semantics

Ordering contexts follow CA-D-637. A verified Project Goal uses its Target Project, while its owner remains the Operator Actor; ordinary endpoints use their Local Scope Unit. The numeric comparison and strict-ancestor rule are unchanged. The exact Project Configuration → Core Meta-Model prerequisite alternative is the logical-role declaration in CA-R-1218; it does not authorize the reverse, another source-role pair, a transitive edge, or a relation from a containing Project or Methodology Sources Scope Unit.
