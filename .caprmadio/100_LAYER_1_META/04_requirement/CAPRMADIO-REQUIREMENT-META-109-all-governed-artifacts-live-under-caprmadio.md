---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-109
scope_path: layer:meta
subject_scope: framework-boundary
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-META-116-preserve-strict-semantic-distinctions
---

# Requirement — Keep every governed artifact under `.caprmadio`

Every governed CAPRMADIO artifact carrier lives inside the current project's
`.caprmadio/` control root. This includes every Atom, Journal, Projection, and
every admitted append-only record sequence, regardless of content role,
governance locus, structural scope, carrier format, or creation mechanism.

An external source may remain outside the project, but any project-governed
reference, adoption record, or other CAPRMADIO artifact about that source lives
under `.caprmadio/`. Git history may retain earlier carrier paths without making
those paths current artifact locations.

`.caprmadio_runtime/`, host temporary storage, product source roots, and external
systems cannot contain the only current carrier of a governed artifact.

## Primary claim

`.caprmadio/` contains every current governed artifact carrier, including
append-only Journals.
