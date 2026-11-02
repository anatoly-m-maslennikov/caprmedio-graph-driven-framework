---
subjects:
  governs: Assess Lineage Impact
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom
  - 'Entity/Node/Continuant/History/Revision/Type: Atom'
  - Subject/Graph/Relation
  - Lineage Impact Analysis
  - 'Entity/Node/Continuant/Actor/Type: Operator'
  - 'Entity/Node/Continuant/Actor/Type: AI Agent'
version: 11
updated_at: 2026-10-23 03:06:32 +0400
relations: {"child_of":["CA-E-002"]}
atom_id: CA-O-058@11
content_role: "Operations"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: Archived
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
---
# Summary

Assess revision impact through lineage

## Operation

Assess Lineage Impact **means** the reusable Action that assesses **every** reachable descendant lineage branch of **`=1`** changed Atom **until** **every** branch has an explicit impact disposition.

apply this Action **when** the Atom:

- receives a new accepted Revision;
- is replaced by a successor; **or**
- moves **to** the archive.

an Operator **or** AI Agent performs this Action within its existing authority. the assessment follows the existing lineage recursively; it does **not** create another cross-Scope Unit dependency graph.

## Details
