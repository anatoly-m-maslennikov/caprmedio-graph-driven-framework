---
subjects:
  governs: Subject/Graph Node.Type
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Term//Property
version: 18
updated_at: 2026-10-26 17:20:40 +0400
relations: {}
atom_id: CA-R-1284@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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