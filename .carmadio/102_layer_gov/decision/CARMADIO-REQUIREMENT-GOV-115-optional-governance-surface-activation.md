---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-115
scope_path: layer:gov
subject_scopes:
  - settings
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-GOV-092
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-090
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-GOV-133
---

# Requirement — Configure optional governance surfaces

`.carmadio/dset_settings.toml` owns one documented `governance_surfaces` table.
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

## Primary claim

Project settings explicitly activate optional governance surfaces, which
default inactive and retain their carriers when deactivated.

## Rationale

The successor preserves progressive adoption while expressing every optional
semantic surface through the current Projection vocabulary.
