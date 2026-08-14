---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-153
scope_path: layer:gov
subject_scope: layout
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-145
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-131
      - CAPRMADIO-REQUIREMENT-META-138
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-100
      - CAPRMADIO-REQUIREMENT-META-109
      - CAPRMADIO-REQUIREMENT-GOV-133
---

# Requirement — Repeat CAPRMADIO role folders in every scope

The `.caprmadio/` root is the implicit project scope. Every project scope and
configured descendant `scope_path` uses the same ordered Content-role folders:

```text
01_concern/
02_analysis/
03_PLAN/
04_REQUIREMENT/
05_METHOD/
06_ASSURANCE/
07_DELIVERY/
08_IMPLEMENTATION/
09_ops/
```

The folder labels use the canonical noun role names. Their numbers express the
CAPRMADIO navigation order only; they do not establish authority, priority,
dependency, lifecycle state, or permission to skip an applicable role.

Every CAPRMADIO Atom, Journal, or Projection carrier is placed in the folder
matching its derived Content role. Native project carriers such as source code,
executable tests, configuration, packages, documentation, and CI workflows
remain in their prescribed project locations outside `.caprmadio/` and are not
copied into the Implementation role folder.

For Atoms, active carriers live directly in the role folder, mutable
pre-admission candidates live under `drafts/`, and inactive admitted carriers
live unchanged under `archive/`. Journals and Projections retain their own
change rules.

Role folders are materialized only when needed. An absent folder is an empty
canonical role slot. Installed external methodology and runtime state remain
outside the governed project-role surface under their separately governed
boundaries.

## Primary claim

Every CAPRMADIO structural scope repeats the ordered `01_concern` through
`09_ops` role surface while native Implementation remains in project-owned
locations outside `.caprmadio/`.

## Rationale

The recursive folder surface makes the nine-role order visible without
confusing the Implementation governance slot with the actual project
realization.
