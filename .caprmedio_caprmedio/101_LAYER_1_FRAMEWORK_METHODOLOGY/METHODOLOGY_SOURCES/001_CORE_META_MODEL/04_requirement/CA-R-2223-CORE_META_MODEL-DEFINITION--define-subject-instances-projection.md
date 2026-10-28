---
atom_id: CA-R-2223
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Subject Graph Instances'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
relations:
  depends_on:
  - CA-R-2150
tier: 2
version: 1
updated_at: 2026-10-27 23:53:05 +0400
---
# Summary

Define Subject Instances Projection

## Claim

A Subject Graph Instances Projection **means** the selected primary Subject hierarchy together with all selected source-backed named instances and declarations, including Workflow instances, Relation Type declarations and concrete Graph Rule declarations. Keep kinds, instance names and the declared Subject operators distinct. Show bare defining Atom IDs, not copied definitions or operative Claim dumps. This view is not a graph of actual Atom-to-Atom Relation tuples and is not a separate property inventory.
