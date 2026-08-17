---
subject_scopes:
  - authority
tier: core
version: 3
updated_at: 2026-08-17 19:48:08
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
---
# Classify RMAD atoms by applicability tier

When a CAPRMADIO project enables applicability-tier classification, each classified Requirement, Method, Assurance, and Delivery Atom resolves to exactly one applicability tier:

- `goal` is the single Project Requirement that states the end CAPRMADIO exists to pursue;
- `principle` is a project-wide invariant that constrains lower tiers and may have no direct application by itself;
- `core` governs the complete declared Project or structural scope; and
- `standard` governs a proper semantic subsegment of its declared scope, such
  as one Content role, Type, subtype, profile, carrier, or relation kind.

Tier is determined by applicability breadth rather than Subject, Type, technicality, implementation detail, or execution order. A project that has not enabled applicability-tier classification omits `tier`.
