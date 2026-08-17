---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-050
scope_path: layer:meta
subject_scope: scope-topology
priority: medium
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-009
      - CAPRMADIO-REQUIREMENT-META-010
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-047
      - CAPRMADIO-REQUIREMENT-META-048
---

# Requirement — Keep product framing optional

User Stories and Outcomes are optional framing constructs rather than semantic
routing axes or mandatory canonical artifact types.

A User Story may frame an actor, desired capability, and value around one or
more Definitions. An intended Outcome may frame a measurable desired state or
assessment target. A measured or reported outcome is an Observation instead of
an intended-state declaration.

Independently enforceable obligations, methods, and checks remain separate
governed artifacts. Framing may link them but cannot replace their authority.

## Rationale

One optional-framing rule preserves familiar product language without forcing
placeholder artifacts or allowing narrative context to hide normative claims.
