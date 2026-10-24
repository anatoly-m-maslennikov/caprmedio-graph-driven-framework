---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Scope Unit Graph'
  depends_on:
  - Primary Entity
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Structural Entity
version: 22
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-R-1407
atom_id: CA-R-834
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Partition project-graph nodes

## Scope

Primary Entity nodes **in** the governed project-containment graph.

## Claim

**every** Primary Entity node **in** the governed project-containment graph **must** belong **to** **`=1`** of the disjoint partitions Artifact **or** Structural Entity.

## Details
