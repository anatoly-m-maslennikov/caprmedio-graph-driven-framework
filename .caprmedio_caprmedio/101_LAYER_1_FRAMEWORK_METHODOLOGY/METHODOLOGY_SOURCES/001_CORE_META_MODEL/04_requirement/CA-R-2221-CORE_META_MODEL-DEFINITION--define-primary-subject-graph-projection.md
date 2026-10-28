---
atom_id: CA-R-2221
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Subject Graph Primary Subjects'
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

Define Primary Subject Graph Projection

## Claim

A Subject Graph Primary Subjects Projection **means** the hierarchy of primary Subject kinds and classification topics from the declared selected sources and Subject branches. It includes the needed ancestor and namespace context, but no dependent-property inventories or named instances. Display only bare defining Atom IDs; authoritative definition text stays in its source Atoms.
