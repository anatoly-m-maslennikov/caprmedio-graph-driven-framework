---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-155
scope_path: layer:gov
subject_scope: artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-141
      - CAPRMADIO-REQUIREMENT-GOV-149
---

# Register the Rationale Analysis subtype

GOV registers `rationale` as a direct subtype of the internal `analysis` Atom Type.

A Rationale Atom owns one primary explanatory conclusion that justifies one or more Requirement, Method, Assurance, or Delivery Atoms. It may preserve material decision grounds, alternatives, trade-offs, implications, and reasons for selecting or rejecting an option.

A Rationale Atom cannot establish or modify normative specification. If an explanation changes an obligation, boundary, selected method, assurance condition, delivery rule, or acceptance meaning, the applicable specification Atom must be created or replaced directly.

Rationale remains optional. Writers must not create an empty or ceremonial Rationale Atom merely to satisfy a template, and sub-subtypes are forbidden.
