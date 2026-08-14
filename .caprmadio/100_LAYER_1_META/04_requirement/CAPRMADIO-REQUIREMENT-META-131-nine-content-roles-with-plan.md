---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-131
scope_path: layer:meta
subject_scope: semantics
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-086
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-080
  - type: relates_to
    targets:
      - CAPRMADIO-ANALYSIS-META-003
      - CAPRMADIO-REQUIREMENT-META-091
      - CAPRMADIO-REQUIREMENT-META-092
      - CAPRMADIO-REQUIREMENT-META-093
      - CAPRMADIO-REQUIREMENT-META-102
---

# Requirement — Use nine Content roles with Plan

CAPRMADIO classifies the primary semantic contribution of governed artifacts
through exactly nine `content_role` values:

1. `concern` identifies a matter requiring disposition.
2. `analysis` develops understanding without independently committing work or
   establishing the desired result.
3. `plan` lists and coordinates one or more action points for changing governed
   artifacts or their realization without itself making those changes.
4. `requirement` states an outcome that the governed product or project must,
   may, or must not provide.
5. `method` specifies how an accepted Requirement will be realized or how an
   existing realization will be transformed.
6. `assurance` specifies how the project can establish that governed claims and
   their realization work as intended.
7. `delivery` specifies how a realized deliverable reaches its users and target
   environments.
8. `implementation` is the concrete native project realization of accepted
   Requirements, Methods, Assurance mechanisms, and Delivery mechanisms.
9. `ops` captures enacted execution and factual results after an Implementation
   is run or used.

The canonical forward loop is:

```text
Concern -> Analysis -> Plan -> Requirement -> Method -> Assurance
        -> Delivery -> Implementation -> Ops -> Concern
```

Requirement, Method, Assurance, and Delivery collectively form the full current
Specification. Plan contains only action points for changing that Specification
or its realization and is not itself part of the Specification. Analysis owns
the findings, alternatives, explanation, and rationale that inform a Plan.
Implementation is the realized project rather than a synonym for its plans,
descriptions, or records.

Artifact form and Governance locus remain independent semantic axes.
`scope_path` remains a structural ownership coordinate.

## Primary claim

CAPRMADIO uses Concern, Analysis, Plan, Requirement, Method, Assurance,
Delivery, Implementation, and Ops as nine distinct Content roles.
