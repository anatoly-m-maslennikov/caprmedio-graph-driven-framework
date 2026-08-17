---
subject_scopes:
  - external-boundary
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-204-review-external-analysis-before-project-adoption
    - CAPRMADIO-REQUIREMENT-GOV-181-represent-accepted-meaning-faithfully
  resolution_of:
    - CAPRMADIO-QUESTION-GOV-015-what-external-review-envelope-is-sufficient
---
# Use external Analysis Atoms as review envelopes

GOV imports an external review as an `external_analysis_report` Atom whose governed envelope identifies its source, provenance, reviewed scope, original body, and native attachments without requiring a provider-specific finding schema. One internal Analysis derives from that Atom, records the project's finding-level interpretation and dispositions, and becomes the only Analysis source from which project-owned Concern, Plan, Requirement, Method, Assurance, or Delivery Atoms are derived. Every accepted disposition that changes project meaning or work is materialized in its owning CPRMAD Content role; rejected or non-actionable findings remain only in the internal Analysis.
