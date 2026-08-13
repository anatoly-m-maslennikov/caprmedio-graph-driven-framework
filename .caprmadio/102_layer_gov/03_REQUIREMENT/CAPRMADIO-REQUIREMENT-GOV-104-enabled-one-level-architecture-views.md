---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-104
scope_path: layer:gov
subject_scopes:
  - layout
tier: standard
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-031
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-090
---

# Requirement — Show one structural level when architecture views are enabled

When a project enables an architecture-view Projection surface, each applicable
project, feature-group, feature, or layer view shows only its immediate enabled
structural children. The project shows feature groups when present, otherwise
features and/or layers; a feature group shows its features; a feature or layer
shows the functions, capabilities, or components directly beneath it.

Each enabled view explains how its level works and how responsibility descends
one level. It links active atomic sources for represented claims and never
claims that navigation creates authority. A disabled surface or absent
structural level requires no placeholder view.

## Primary claim

Enabled architecture views show one structural level down; disabled views and
absent levels create no artifact obligation.

## Rationale

The successor preserves readable helicopter views while aligning their
existence with optional Projection surfaces.
