---
subject_scopes:
  - artifact-catalog
project_settings:
  artifacts:
    enabled_types:
      - requirement:principle
      - method:principle
      - evaluation:principle
      - delivery:principle
      - ops:principle
version: 1
updated_at: 2026-08-20 05:09:11
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-658--define-principle-applicability-tier
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register Principle Types across RMEDO

GOV registers one role-specific internal Principle Type in each RMEDO Content role. Every RMEDO Atom whose derived global tier is `0` uses its role's Principle Type, and no Atom at another global tier uses a Principle Type.
