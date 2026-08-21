---
subject_scopes:
  - artifact-model
version: 2
updated_at: 2026-08-21 20:51:16
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-192--explicit-relational-endpoints
  child_of:
    - CAPRMEDIO-META-REQU-127--define-three-governance-loci
---
# Represent graph relations in frontmatter

## Primary claim

Every relation in the governed graph is a typed edge declared under the
relation-owning Atom's `relations` frontmatter. A relation is not an Artifact,
Governance origin, or Artifact Type merely because it connects graph nodes.

An Atom whose governed content concerns a contract, conflict, binding, or
another relationship remains an ordinary Atom. Its graph connections use the
same frontmatter relation mechanism as every other Atom.
