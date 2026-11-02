---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Scope Unit Graph'
  depends_on:
  - Primary Entity
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Structural Entity
version: 20
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-R-834-CORE_META_MODEL-CORE-REQUIREMENT--partition-project-graph-nodes
atom_id: CA-R-836@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Encode project-graph node partitions

## Scope

governed project-containment graph nodes.

## Claim

the project-containment graph **must** derive **`=1`** partition for **every** governed Primary Entity node from its Artifact **or** Structural Entity classification **and** reject a node whose partition count is **`!=1`**.

## Details
