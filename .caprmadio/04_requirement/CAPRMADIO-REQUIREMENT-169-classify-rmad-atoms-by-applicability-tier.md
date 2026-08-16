---
subject_scopes:
  - authority
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
---

# Classify RMAD Atoms by applicability tier

Every Requirement, Method, Assurance, and Delivery Atom resolves to exactly one
applicability tier:

- `principle` is a project-wide invariant that constrains lower tiers and may
  have no direct application by itself;
- `core` governs the complete declared project, Layer, or Feature scope; and
- `standard` governs a proper semantic subsegment of its declared scope, such
  as one Content role, Type, subtype, profile, carrier, or relation kind.

Tier is determined by applicability breadth rather than Subject, Type,
technicality, implementation detail, or execution order.
