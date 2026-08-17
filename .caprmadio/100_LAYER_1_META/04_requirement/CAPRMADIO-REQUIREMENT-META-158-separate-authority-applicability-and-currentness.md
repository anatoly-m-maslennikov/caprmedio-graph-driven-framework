---
subject_scopes:
  - authority
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-189-configurability-selects-available-capabilities
---
# Separate authority applicability and currentness

Authority is an Artifact's governed capacity to establish meaning of a declared kind. Applicability determines whether that meaning governs a particular structural scope, profile, environment, version, time boundary, or other declared context. Currentness determines which exact applicable Artifact revision is presently effective in that context.

These properties are orthogonal. An authoritative Artifact may be inapplicable to a given context; an applicable historical revision may no longer be current; and a current Projection may accurately report state without possessing semantic authority. Acceptance, provenance, implementation, evidence, and assurance do not silently establish authority, applicability, or currentness.

Precedence and conflict resolution select among otherwise authoritative and applicable claims; they do not merge these properties. GOV owns the concrete rules and generated views used to resolve and report them.
