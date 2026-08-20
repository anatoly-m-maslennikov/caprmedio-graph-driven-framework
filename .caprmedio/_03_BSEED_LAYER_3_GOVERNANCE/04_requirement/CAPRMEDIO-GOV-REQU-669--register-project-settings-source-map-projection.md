---
subject_scopes:
  - settings
version: 4
updated_at: 2026-08-19 04:55:53
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-666--register-project-settings-source-map-atom
    - CAPRMEDIO-GOV-REQU-667--bind-project-settings-source-map-revisions-in-the-work-journal
  child_of:
    - CAPRMEDIO-REQU-646--govern-project-settings-projection-through-framework-methodology
    - CAPRMEDIO-META-REQU-166--projections-have-updated-at
    - CAPRMEDIO-META-REQU-627--bind-every-projected-setting-to-exact-source-authority
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register the Project Settings Source Map Projection

GOV must register `.caprmedio/08_implementation/CAPRMEDIO-MAPS-001--project-settings-source-map.yaml` as the versionless internal Projection with Content role `implementation` and Type `map` that is generated from the same active RMED contributions as Project Settings, maps every emitted leaf key to its exact contributing Atom revisions, records `updated_at` and the source frontier, and is never read as authority for values or source selection.

This Projection uses YAML as an explicit exception to the default TOML technical carrier. Its required representation is a compact, deeply nested tree that mirrors the setting paths embedded in Atom YAML frontmatter and keeps shared ancestry visible without repeating a TOML table path for every branch. The Projection remains generated, read-only, and non-authoritative; it does not create a parallel writable YAML settings source.
