---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-106
scope_path: layer:gov
subject_scopes:
  - layout
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-GOV-053
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-053
      - CARMADIO-REQUIREMENT-META-090
---

# Requirement — Keep durable hubs folder-level

A durable hub may directly list stable child areas and their hubs, folders that
contain Atoms, enabled Projections, settings, and other long-lived governed
carriers.

A hub never enumerates individual atomic carriers. Adding an atom therefore
does not require a hub edit. A hub also never lists or links descendants of
`.dset_runtime` or `.dset_journal`; runtime state and high-churn journal
records are discoverable through their own tools and governed views.

## Primary claim

Hubs navigate stable folders and long-lived governed carriers without
enumerating atoms, runtime state, or journal records.

## Rationale

Folder-level navigation stays current as immutable atoms and append-only
records accumulate.
