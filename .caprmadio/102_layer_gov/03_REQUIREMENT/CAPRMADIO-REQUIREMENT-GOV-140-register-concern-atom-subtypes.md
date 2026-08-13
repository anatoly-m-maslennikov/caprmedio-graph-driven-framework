---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-140
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-086
      - CAPRMADIO-REQUIREMENT-GOV-138
---

# Requirement — Register Concern Atom subtypes

GOV registers these direct subtypes of the internal Concern Atom Type:

- `question` records an unresolved matter whose answer may change governed
  understanding or action;
- `problem` asserts a present undesirable condition requiring disposition;
- `risk` records a possible future undesirable condition with a trigger or
  uncertainty boundary; and
- `opportunity` records an optional improvement whose expected value does not
  establish a present defect or obligation.

A relational disagreement between explicit endpoints uses the relational
`conflict` Type rather than an internal Concern subtype. Defect, gap, debt, and
other more specific labels remain descriptions until GOV admits them as direct
subtypes; sub-subtypes are forbidden.

## Primary claim

`question`, `problem`, `risk`, and `opportunity` are the currently registered
direct subtypes of the internal Concern Atom Type.

## Rationale

The four subtypes distinguish missing knowledge, present harm, possible future
harm, and optional value without creating separate top-level Types or deriving
artifact identity from workflow state.
