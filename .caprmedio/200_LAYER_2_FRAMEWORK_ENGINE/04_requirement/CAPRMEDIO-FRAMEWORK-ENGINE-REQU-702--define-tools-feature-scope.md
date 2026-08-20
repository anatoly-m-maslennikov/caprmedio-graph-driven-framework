---
subject_scopes:
  - feature-boundary
version: 4
updated_at: 2026-08-20 22:58:24
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-SPEC-REQU-499--define-tools-feature-scope
    - CAPRMEDIO-REALIZATION-REQU-592--define-tools-feature-scope
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-700--define-framework-engine-feature-topology
---
# Define the TOOLS Feature scope

The FRAMEWORK_ENGINE Feature with scope `tools`, full name `TOOLS`, and prefix `TOOLS` owns independently executable Tools classified by behavior as Hooks, Finders, or Doers, with Checkers governed as a Finder specialization rather than as a separate structural unit. Hooks emit triggers into Tool flows and have no read, classification, or mutation authority beyond observing their registered boundary.
