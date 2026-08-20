---
subject_scopes:
  - project-settings
tier: core
version: 3
updated_at: 2026-08-19 16:45:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-674--derive-project-settings-and-map-from-rmed
---
# Compose Project Settings from RMED contributions

Enumerate active RMED Atom carriers, parse each optional `project_settings` map, flatten its scalar and list leaves to dotted setting paths, require one contributor for each scalar leaf, concatenate list fragments by canonical source identity while rejecting duplicate items, then render Project Settings values and Map bindings from that single composed state and replace both outputs atomically only after the complete state validates.
