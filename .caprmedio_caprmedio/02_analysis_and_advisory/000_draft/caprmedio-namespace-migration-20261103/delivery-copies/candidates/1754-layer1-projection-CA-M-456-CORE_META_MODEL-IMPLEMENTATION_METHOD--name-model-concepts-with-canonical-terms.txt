---
atom_id: CA-M-456
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Node
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-456-CORE_META_MODEL-IMPLEMENTATION_METHOD--name-model-concepts-with-canonical-terms.md
  source_atom_id: CA-M-456
  source_atom_revision: 2
  source_sha256: 4a01421a55ecebf6e5907127e8093121b93da5cfbe5819160bae6b556451c4a5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Name Model Concepts with Canonical Terms

## Claim scope

Authoring names for metamodel and Project concepts.

## Claim

- Choose names that distinguish their referents.
- Avoid Entity, Type, Content or Value when they add no information.
- Keep useful qualified and compound expressions.
- Use one canonical Term per concept across prose, formal paths and YAML.
- Do not introduce unnecessary synonyms or replace words globally.

## Details

Choose a name from the concept it denotes, not from a neighboring carrier or implementation. For example, prefer `Form` when distinguishing Declaration from other Requirement forms, and `Node` when naming a graph member. Retain `Entity Definition` or `Atom Content` where the established compound expresses the intended concept; do not replace words globally without an approved mapping.
