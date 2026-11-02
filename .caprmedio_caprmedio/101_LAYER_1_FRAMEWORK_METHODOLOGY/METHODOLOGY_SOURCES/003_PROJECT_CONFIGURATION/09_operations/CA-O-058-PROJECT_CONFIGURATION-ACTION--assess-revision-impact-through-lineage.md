---
subjects:
  governs: Subject/caprmedio/Action//Assess Lineage Impact
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Version Number
  - Subject/CAPRMEDIO/Graph/Relation
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Analysis'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
version: 19
updated_at: 2026-10-30 00:32:29 +0400
relations: {}
atom_id: CA-O-058
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
type: Action
tier: 3
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
