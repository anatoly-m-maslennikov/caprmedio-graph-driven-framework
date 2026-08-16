---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-145
scope_path: layer:meta
subject_scopes:
  - artifact-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-121-bind-traceability-to-exact-claims-and-revisions
    - CAPRMADIO-REQUIREMENT-META-128-bind-governed-transactions-to-stable-artifact-revisions
---

# Let the dependent Atom own the relation

When one Atom depends semantically on a pre-existing artifact, the dependent Atom stores the directed relation to that upstream subject. Creating the dependent Atom must not require modifying the upstream artifact.

The relation direction records dependency and provenance, not the visual order of CAPRMADIO Content roles. A later-created Rationale may therefore point to an earlier-created Requirement even though Analysis precedes Requirement in the framework mnemonic.

The dependent Atom stores the only persisted relation to its pre-existing semantic subject.
