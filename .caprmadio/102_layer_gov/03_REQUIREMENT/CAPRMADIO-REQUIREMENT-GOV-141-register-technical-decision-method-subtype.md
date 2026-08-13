---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-141
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
tier: standard
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-086
      - CAPRMADIO-REQUIREMENT-GOV-138
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-136
---

# Requirement — Register Technical Decision as a Method subtype

GOV registers `technical_decision` as a direct subtype of the internal Method
Atom Type.

A Technical Decision selects one bounded technical approach, structure,
algorithm, dependency, protocol, or realization rule from viable alternatives.
It explains the selected approach and applicable tradeoffs without redefining
the required outcome, recording the realized change, or claiming assurance or
operational results.

An accepted strategy for one bounded transformation uses the more specific
`refactoring_plan` subtype. A decision that exists between explicit endpoints
uses the relational `integration_decision` Type.

## Primary claim

`technical_decision` is a direct internal Method subtype for one bounded
technical realization choice.

## Rationale

The subtype gives implementation choices a precise home while keeping outcome
Requirements, relational Integration Decisions, concrete Implementations, and
Refactoring Plans independently replaceable.
