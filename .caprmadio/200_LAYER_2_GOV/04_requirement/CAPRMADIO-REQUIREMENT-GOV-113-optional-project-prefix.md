---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-113
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-064
  relates_to:
    - CAPRMADIO-REQUIREMENT-GOV-108
---
# Configure an optional project prefix

`.caprmadio/caprmadio_settings.toml` records whether artifact identities use a project
prefix and records its value when enabled.

Project initialization recommends:

- no prefix for one small project with one artifact namespace; and
- a prefix for a monorepo, multiple CAPRMADIO projects in one repository, or any
  shared namespace where otherwise valid identities could collide.

Changing the setting after governed identities exist requires one complete
lossless whole-graph migration. It updates active and archived identities,
filenames, relations, Projection and Journal references, settings,
Implementation references, Ops records, and commit provenance together. The
project never retains two accepted identity vocabularies.

## Rationale

A small single-project repository gains no disambiguation from a mandatory
prefix, while a shared namespace requires one.
