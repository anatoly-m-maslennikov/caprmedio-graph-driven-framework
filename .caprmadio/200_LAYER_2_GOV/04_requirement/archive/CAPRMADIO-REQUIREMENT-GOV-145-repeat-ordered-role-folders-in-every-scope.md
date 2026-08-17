---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-145
scope_path: layer:gov
subject_scopes:
  - layout
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-120
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-086
      - CAPRMADIO-REQUIREMENT-META-100
      - CAPRMADIO-REQUIREMENT-META-109
  - type: relates_to
    targets:
      - CAPRMADIO-PROBLEM-GOV-011
      - CAPRMADIO-REQUIREMENT-GOV-133
---

# Requirement — Repeat ordered Content-role folders in every scope

The `.caprmadio/` root is the implicit project scope. It contains project-level governed carriers directly and does not wrap them in a `project/` or `100_project/` directory. Every project scope and every configured descendant `scope_path`, including layers, feature groups, features, and their permitted nesting, uses the same ordered Content-role folders:

```text
01_concern/
02_analysis/
03_requirement/
04_method/
05_assurance/
06_delivery/
08_implementation/
08_ops/
```

The numbers express the canonical CAPRMADIO navigation order only. They do not establish authority, priority, dependency, lifecycle order, or permission to skip an applicable role.

Every CAPRMADIO Atom, Journal, or Projection carrier is placed in the folder matching its derived Content role. Artifact form, Type, subtype, and Governance locus remain governed by identity and registered metadata rather than additional path levels. Native project carriers such as source code, executable tests, configuration, packages, and CI workflows remain in their prescribed project locations and are not copied into `.caprmadio/`.

For Atoms, the role folder is also the lifecycle boundary: an admitted active carrier lives directly in the role folder, a mutable pre-admission candidate lives under its role-local `drafts/`, and an inactive admitted carrier lives unchanged under its role-local `archive/`. Journals and Projections use their own change rules and are not assigned an Atom lifecycle state merely because they share the role folder.

Layer, feature-group, and feature scope directories retain their registered structural identities and repeat the same role-folder surface recursively. A narrower scope may contain another configured scope kind without changing either scope identity or Content-role meaning. Role folders and their `drafts/` or `archive/` children are materialized only when needed; an absent folder is treated as an empty canonical role slot.

The installed external methodology remains under its reserved `000_caprmadio_framework/` boundary. Runtime and host-scratch state remain outside the governed role-folder tree.

## Primary claim

The project root and every descendant structural scope organize governed CAPRMADIO carriers through the same ordered, role-local `01_concern` through `08_ops` folder surface while native implementation remains in its project-owned locations.

## Rationale

One recursive role surface makes the CAPRMADIO order visible at every scope, removes legacy family and Type-folder ambiguity, and avoids deep folder multiplication for external, relational, and subtype variants that already have canonical identities.
