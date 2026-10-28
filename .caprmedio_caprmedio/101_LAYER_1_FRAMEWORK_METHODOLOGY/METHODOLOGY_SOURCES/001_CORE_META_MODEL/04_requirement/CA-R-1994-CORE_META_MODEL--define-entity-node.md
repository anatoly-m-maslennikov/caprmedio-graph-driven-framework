---
atom_id: CA-R-1994
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model
relations: {}
version: 11
updated_at: 2026-10-27 20:00:07 +0400
tier: 1
type: Definition
---
# Summary

Define Entity/Node

## Scope

Nodes in the Subject graph.

## Claim

A Node identifies a thing or topic addressed by the graph. Its description and Carrier are separate.

## Semantics

Subjects intentionally include actual things, descriptions and abstract topics. This mix does not make them one uniform kind of entity. A description can itself be a separate Subject; it is not the thing described.

Artifact is a Term for a Node instance delivered into one or more Carrier instances. Carrying a record of an occurrence does not carry the actual occurrence. Artifact does not name another Node kind or branch. A Carrier remains distinct from what it represents.

## Details

Graph Node categories are open. Continuant, Occurrent and Aspect are admitted category examples, not an exhaustive enumeration. A topic does not need to be forced into a temporal category.
