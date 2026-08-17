---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-104
scope_path: layer:meta
subject_scope: scope-topology
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
---
# Requirement — Propagate structural scope through realization

## Primary claim

A project structural scope is registered once and reused unchanged by every
realization layer that governs it. Layer-local subject scopes may refine its
meaning but never redefine its structural identity.
