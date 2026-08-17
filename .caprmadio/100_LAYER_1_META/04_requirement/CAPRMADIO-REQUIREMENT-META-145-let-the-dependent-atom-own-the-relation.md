---
subject_scopes:
  - artifact-model
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-182-the-graph-is-the-operating-model
---
# Let the dependent atom own the relation

When one Atom depends semantically on a pre-existing artifact, the dependent Atom stores the directed relation to that upstream subject. Creating the dependent Atom must not require modifying the upstream artifact.

The relation direction records dependency and provenance, not the visual order of CAPRMADIO Content roles. A later-created Rationale may therefore point to an earlier-created Requirement even though Analysis precedes Requirement in the framework mnemonic.

The dependent Atom stores the only persisted relation to its pre-existing semantic subject.
