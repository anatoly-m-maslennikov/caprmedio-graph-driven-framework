---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-109
scope_path: layer:meta
subject_scopes:
  - governance-surface
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-080
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-053
      - CARMADIO-REQUIREMENT-META-076
---

# Requirement — Keep every governed artifact under `.carmadio`

Every governed CARMADIO artifact carrier lives inside the current project's
`.carmadio/` control root. This includes every Atom, Journal, Projection, and
every admitted append-only record sequence, regardless of content role,
governance locus, structural scope, carrier format, or creation mechanism.

An external source may remain outside the project, but any project-governed
reference, adoption record, or other CARMADIO artifact about that source lives
under `.carmadio/`. Git history may retain earlier carrier paths without making
those paths current artifact locations.

`.carmadio_runtime/`, host temporary storage, product source roots, and external
systems cannot contain the only current carrier of a governed artifact.

## Primary claim

`.carmadio/` contains every current governed artifact carrier, including
append-only Journals.

## Rationale

One bounded control root makes artifact discovery complete without conflating
governed history with disposable execution state.
