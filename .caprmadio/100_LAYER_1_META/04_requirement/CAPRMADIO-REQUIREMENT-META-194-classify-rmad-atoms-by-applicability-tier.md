---
subject_scopes:
  - authority
tier: core
version: 5
updated_at: 2026-08-17 22:35:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-242-organize-authority-as-a-hierarchical-graph
---
# Classify RMAD atoms by applicability tier

When a CAPRMADIO project enables applicability-tier classification, each classified Requirement, Method, Assurance, and Delivery Atom resolves to exactly one readable tier name in the project-configured ordered tier catalog.

The Project Goal is a Requirement subtype outside the ordered applicability-tier catalog and occupies global tier `-1`. Project applicability-tier positions begin at `0` and are derived from catalog order rather than stored in Atoms. The current catalog is:

- `principle` at depth `0`, a project-wide invariant that constrains deeper tiers and may have no direct application by itself;
- `core` at depth `1`, governing the complete declared Project or structural scope; and
- `standard` at depth `2`, governing a proper semantic subsegment of its declared scope, such as one Content role, Type, subtype, Profile, carrier, or relation kind.

Projects and Extensions may register additional uniquely named tiers. Tier position is determined by configured applicability order rather than Subject, Type, technicality, implementation detail, or execution order. Atoms store readable tier names rather than numeric depths. A project that has not enabled applicability-tier classification omits `tier`.
