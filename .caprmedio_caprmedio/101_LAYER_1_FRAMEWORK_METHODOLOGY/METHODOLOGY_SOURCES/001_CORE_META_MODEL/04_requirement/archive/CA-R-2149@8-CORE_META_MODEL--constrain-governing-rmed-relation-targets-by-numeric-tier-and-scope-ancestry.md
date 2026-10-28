---
subjects:
  governs: Subject/Graph Rule
  depends_on:
  - Subject/Graph Rule.Type
  - Subject/Graph Rule.Applies To
  - Subject/Graph Rule.Condition
  - Subject/Graph Node/Domain/Continuant/Selection//Stored Governing RMED Relation Occurrences
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
  - Subject/Graph Node/Domain/Continuant/Scope Unit
relations: {}
atom_id: CA-R-2149@8
content_role: Requirement
type: Graph Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-26 05:29:36 +0400
claim:
  graph_rule_type: endpoint_constraint
  applies_to:
    relation_selection: Subject/Graph Node/Domain/Continuant/Selection//Stored Governing RMED Relation Occurrences
  condition:
    ordering: same_scope_lower_target_tier_or_strict_ancestor_or_project_configuration_core_prerequisite
---
# Summary

Constrain Governing RMED Relation Targets by Numeric Tier and Scope Ancestry

## Semantics

Ordering contexts follow CA-D-637. A verified Project Goal uses its Target Project, while its owner remains the Operator Actor; ordinary endpoints use their Local Scope Unit. The numeric comparison and strict-ancestor rule are unchanged. The exact Project Configuration → Core Meta-Model prerequisite alternative is the logical-role declaration in CA-R-1218; it does not authorize the reverse, another source-role pair, a transitive edge, or a relation from a containing Project or Methodology Sources Scope Unit.
