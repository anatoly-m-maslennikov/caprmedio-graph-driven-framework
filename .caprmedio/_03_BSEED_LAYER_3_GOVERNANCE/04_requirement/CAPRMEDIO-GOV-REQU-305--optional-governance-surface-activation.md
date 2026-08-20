---
subject_scopes:
  - settings
project_settings:
  governance_surfaces:
    architecture_view: false
    project_overview: false
    relation_map: false
    requirement_catalog: false
    scope_hub: false
version: 2
updated_at: 2026-08-18 20:19:17
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-448--governance-surface-settings
  relates_to:
    - CAPRMEDIO-GOV-REQU-313--govern-catalog-map-and-hub-projections
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Configure optional governance surfaces

`.caprmedio/caprmedio_project_settings.toml` owns one documented `governance_surfaces` table.
Every registered optional surface has one explicit boolean. The initial
surface keys are:

- `requirement_catalog`;
- `relation_map`;
- `scope_hub`;
- `project_overview`; and
- `architecture_view`.

All values default to `false`; missing configuration has the same atomic-first
meaning. Unknown surface names fail closed.

Activation makes a surface applicable to its currentness and downstream gates.
Deactivation removes those obligations without deleting or archiving its
Projection carrier. Retained files become inactive references until
reactivation reconciles them against current atomic authority.

## Rationale

The successor preserves progressive adoption while expressing every optional
semantic surface through the current Projection vocabulary.
