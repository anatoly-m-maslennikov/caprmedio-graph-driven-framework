---
atom_id: CA-R-2149@10-draft
ref_id: CA-R-2149@10-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Graph Rule
topics:
  main_subject: Formal Model::CAPRMEDIO::Graph Rule
  dependencies:
  - Subject/CAPRMEDIO/Graph/Rule.Type
  - Subject/CAPRMEDIO/Graph/Rule.Applies To
  - Subject/CAPRMEDIO/Graph/Rule.Condition
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Stored Governing RMED Relation Occurrences
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Header.Context.Tier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
tier: 1
status: Draft
version: 10
updated_at: 2026-10-28 19:24:50 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
# Summary

Constrain Governing RMED Relation Targets by Numeric Tier and Scope Ancestry

## Claim

```yaml
graph_rule_type: endpoint_constraint
applies_to:
  relation_selection: Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Stored Governing RMED Relation Occurrences
condition:
  ordering: same_scope_lower_target_tier_or_strict_ancestor_or_project_configuration_core_prerequisite
```

## Semantics

Ordering contexts follow CA-D-637. A verified Project Goal uses its Target Project, while its owner remains the Operator Actor; ordinary endpoints use their Local Scope Unit. The numeric comparison and strict-ancestor rule are unchanged. The exact Project Configuration → Core Meta-Model prerequisite alternative is the logical-role declaration in CA-R-1218; it does not authorize the reverse, another source-role pair, a transitive edge, or a relation from a containing Project or Methodology Sources Scope Unit.

## Details

Superseded preparation: CA-A-1242 removes the special Graph Rule branch and Atom Type. Do not promote this legacy Graph Rule packet entry as written. Preserve its useful formal constraints/schema evidence for incorporation into the appropriate Definition Claims; no Current rule or predecessor is deleted by this marker.
