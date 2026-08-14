---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-141
scope_path: layer:meta
subject_scope: artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-131
      - CAPRMADIO-REQUIREMENT-META-135
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-092
      - CAPRMADIO-REQUIREMENT-META-140
---

# Requirement — Place rationale in Analysis

Rationale is interpretive justification and belongs to the Analysis Content role. Requirement, Method, Assurance, and Delivery artifacts own normative specification and must not embed a `Rationale` section or duplicate rationale metadata.

When material rationale is worth preserving, one Analysis Atom owns one primary explanatory conclusion and relates it to one or more applicable specification Atoms. Rationale is optional: an obvious claim does not require an Analysis Atom merely to satisfy a template.

If explanatory text changes an obligation, boundary, selected method, assurance condition, delivery rule, or acceptance meaning, that text is normative rather than rationale and remains in the applicable specification Atom.

## Primary claim

Material rationale is optional Analysis linked to specification artifacts; it is never embedded normative specification content.
