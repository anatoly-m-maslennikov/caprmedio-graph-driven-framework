---
subjects:
  - lifecycle-traceability
version: 4
updated_at: 2026-08-23 01:44:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-618--separate-framework-and-project-configuration
    - CAPRMEDIO-REQU-007--full-minimal-traceability
---
# Bind every projected Graph State value to exact sources

Every value emitted into a Project Graph State Projection must be computed from and bind to the exact Project Configuration Atom revision and exact applicable source Atom revisions and Journal records. Generation fails when a required source is missing, malformed, unresolved, ambiguous, stale, or contradictory.
