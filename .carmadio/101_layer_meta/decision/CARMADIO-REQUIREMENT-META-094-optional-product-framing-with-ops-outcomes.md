---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-094
scope_path: layer:meta
subject_scopes:
  - product-framing
priority: medium
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-050
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-086
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-092
---

# Requirement — Keep product framing optional

User Stories and Outcomes are optional framing constructs rather than semantic routing axes or mandatory canonical artifact types.

A User Story may frame an actor, desired capability, and value around one or more Requirements. An intended Outcome may frame a measurable required state or assessment target. A measured or reported outcome is an Ops fact instead of a Requirement.

Independently enforceable Requirements, Methods, Assurance criteria, and Delivery rules remain separate governed artifacts. Framing may link them but cannot replace their authority.

## Primary claim

User Stories and intended Outcomes remain optional framing, while measured or reported outcomes are Ops facts.

## Rationale

One optional-framing rule preserves familiar product language without forcing placeholder artifacts or allowing narrative context to hide normative claims.
