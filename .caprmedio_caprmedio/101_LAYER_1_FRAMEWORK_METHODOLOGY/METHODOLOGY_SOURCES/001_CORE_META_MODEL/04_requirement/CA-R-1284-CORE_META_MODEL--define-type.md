---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
version: 19
updated_at: 2026-10-27 19:59:53 +0400
relations: {}
atom_id: CA-R-1284
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Type

## Scope

Type Properties and their applicable allowed-value sets for Graph Nodes. A Graph Node may omit a Type unless an applicable governing rule requires one.

## Claim

a Type **means** a single-valued Property **when** a Graph Node admits that Type Property; its applicable allowed-value set is finite at one Applicable Methodology Revision **and** expandable through governed Methodology Sources. Type is optional for Graph Nodes generally; a specific governing rule **may** require `Atom.Type` or another explicitly scoped Type Property.

## Details

The allowed-value set is scoped to the governed Property and Applicable Methodology Revision. General Graph Node optionality does not prevent a specific governing rule from requiring a Type Property for its subject.