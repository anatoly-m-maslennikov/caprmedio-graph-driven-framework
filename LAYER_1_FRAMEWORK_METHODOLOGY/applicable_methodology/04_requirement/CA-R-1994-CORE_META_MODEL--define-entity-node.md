---
atom_id: CA-R-1994
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Entity
  passive:
  - CAPRMEDIO_MODEL <+ Node/Continuant
relations: {}
version: 15
updated_at: 2026-11-02 00:18:22 +0400
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1994-CORE_META_MODEL--define-entity-node.md
  source_atom_id: CA-R-1994
  source_atom_revision: 15
  source_sha256: daf5b426d708893c865ef6394b3a3ea5d0e71f01367f8208d49694e92225f06f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Entity/Node

## Claim

### Prose Claim


Nodes in the Subject graph.



An Entity used as a Subject-graph node must identify a thing or topic addressed by the graph; its description and Carrier remain separate.

## Semantics

Subjects intentionally include actual things, descriptions and abstract topics. This mix does not make them one uniform kind of entity. A description can itself be a separate Subject; it is not the thing described.

Artifact is a Term for a Node instance delivered into one or more Carrier instances. Carrying a record of an occurrence does not carry the actual occurrence. Artifact does not name another Node kind or branch. A Carrier remains distinct from what it represents.

## Details

Graph Node categories are open. Continuant, Occurrent and Aspect are admitted category examples, not an exhaustive enumeration. A topic does not need to be forced into a temporal category.
