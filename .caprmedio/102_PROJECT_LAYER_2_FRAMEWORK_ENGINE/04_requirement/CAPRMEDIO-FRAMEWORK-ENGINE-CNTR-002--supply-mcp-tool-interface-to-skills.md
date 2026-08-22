---
subject_scopes:
  - scope-topology
semantic_shape: relational
version: 2
updated_at: 2026-08-22 01:56:15
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relational_endpoints:
  controller:
    scope_unit: ./SKILLS
    content_role: requirement
  followers:
    - scope_unit: ./MCP
      content_roles:
        - delivery
relations:
  child_of:
    - CA-R-881-REQUIREMENT--own-cross-unit-relational-atoms-at-the-common-scope
  realization_input:
    - ./MCP
  depends_on:
    - ./MCP
---
# Supply the MCP Tool interface to SKILLS

MCP supplies SKILLS with the current generated discovery and invocation interface for active Tools. Skills select and use that interface without redefining Tool behavior, while MCP preserves each Tool's identity, accepted inputs, structured outputs, and failure meaning.
