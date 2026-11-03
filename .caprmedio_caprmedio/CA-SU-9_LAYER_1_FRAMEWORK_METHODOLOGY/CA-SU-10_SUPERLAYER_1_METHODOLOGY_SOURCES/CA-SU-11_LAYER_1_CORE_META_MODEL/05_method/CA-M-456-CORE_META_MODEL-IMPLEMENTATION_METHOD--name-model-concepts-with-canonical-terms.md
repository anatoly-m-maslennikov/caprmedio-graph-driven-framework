---
atom_id: CA-M-456
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Node
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Method
form: Implementation Method
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
