---
atom_id: CA-R-1994
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
  passive:
  - CAPRMEDIO <+ MODEL <+ Node/Continuant
relations: {}
version: 15
updated_at: 2026-11-02 00:18:22 +0400
tier: 1
role: Requirement
form: Rule
---
## Summary

Define Entity/Node

## Claim scope

Nodes in the Subject graph.

## Claim


An Entity used as a Subject-graph node must identify a thing or topic addressed by the graph; its description and Carrier remain separate.

## Semantics

Subjects intentionally include actual things, descriptions and abstract topics. This mix does not make them one uniform kind of entity. A description can itself be a separate Subject; it is not the thing described.

Artifact is a Term for a Node instance delivered into one or more Carrier instances. Carrying a record of an occurrence does not carry the actual occurrence. Artifact does not name another Node kind or branch. A Carrier remains distinct from what it represents.

## Details

Graph Node categories are open. Continuant, Occurrent and Aspect are admitted category examples, not an exhaustive enumeration. A topic does not need to be forced into a temporal category.
