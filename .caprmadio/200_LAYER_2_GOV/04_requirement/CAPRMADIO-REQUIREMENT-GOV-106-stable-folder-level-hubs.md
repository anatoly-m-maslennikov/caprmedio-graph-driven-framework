---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-106
scope_path: layer:gov
subject_scopes:
  - layout
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-053
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-181
---
# Keep durable hubs folder-level

A durable hub may directly list stable child areas and their hubs, folders that
contain Atoms, enabled Projections, settings, and other long-lived governed
carriers.

A hub never enumerates individual atomic carriers. Adding an atom therefore
does not require a hub edit. A hub also never lists or links descendants of
`.caprmadio_runtime`; runtime state and individual high-churn Journal records are
discoverable through their own tools and governed Projections.

## Rationale

Folder-level navigation stays current as immutable atoms and append-only
records accumulate.
