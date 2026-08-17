---
subject_scopes:
  - scope-topology
tier: core
version: 2
updated_at: 2026-08-17 20:02:25
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-207-assign-feature-scope-ownership-to-each-layer
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-242-organize-authority-as-a-hierarchical-graph
---
# Model project structure as numbered levels

CAPRMADIO must model project structure as the Project root followed by zero or more numbered structural levels, with every non-root scope occupying one level and owned by exactly one parent scope in the immediately preceding level.
