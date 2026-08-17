---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-155
scope_path: layer:gov
subject_scope: artifact-catalog
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-181
---
# Register the Rationale Analysis subtype

GOV registers `rationale` as a direct subtype of the internal `analysis` Atom Type.

A Rationale Atom owns one primary explanatory conclusion that justifies one or more Requirement, Method, Assurance, or Delivery Atoms. It may preserve material decision grounds, alternatives, trade-offs, implications, and reasons for selecting or rejecting an option.

A Rationale Atom cannot establish or modify normative specification. If an explanation changes an obligation, boundary, selected method, assurance condition, delivery rule, or acceptance meaning, the applicable specification Atom must be created or replaced directly.

Rationale remains optional. Writers must not create an empty or ceremonial Rationale Atom merely to satisfy a template, and sub-subtypes are forbidden.
