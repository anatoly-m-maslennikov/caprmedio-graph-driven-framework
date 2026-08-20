---
subject_scopes:
  - semantics
tier: core
version: 3
updated_at: 2026-08-21 00:21:06
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-162--govern-configuration-semantics
  child_of:
    - CA-O-002-PRINCIPLE-OPS--select-optional-capabilities-through-configuration
---
# Separate Project Configuration from Project Graph State

CAPRMEDIO must distinguish the human-editable Project Configuration Atom from generated Project Graph State Projections. Only the Configuration Atom is settings and owns operator-selected values; Graph State Projections are read-only derived views and never configuration authority.
