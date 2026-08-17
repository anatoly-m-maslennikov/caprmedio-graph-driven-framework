---
subject_scopes:
  - artifact-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-154-three-artifact-forms-with-generated-projections
    - CAPRMADIO-REQUIREMENT-META-157-separate-artifact-carrier-and-revision
---
# Give Atoms explicit revision ordinals

Every Atom revision carries one positive monotonic ordinal scoped to its stable Artifact identity and one unambiguous time identifying when that revision was created. Creation starts a new identity at ordinal one, every governed carrier-content edit advances the ordinal exactly once, replacement starts the successor identity at one, and a path-only lifecycle move does not create a content revision.
