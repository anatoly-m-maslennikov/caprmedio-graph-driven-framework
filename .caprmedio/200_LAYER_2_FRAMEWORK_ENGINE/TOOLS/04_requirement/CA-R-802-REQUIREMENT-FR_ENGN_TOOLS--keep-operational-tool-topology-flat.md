---
subject_scopes:
  - feature-boundary
tier: core
version: 4
updated_at: 2026-08-20 22:58:24
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-702--define-tools-feature-scope
---
# Keep operational Tool topology flat

Operational Tools must be peer `unordered_unit` Structural units owned immediately by `TOOLS`; `Hook`, `Finder`, and `Doer` classify Tool behavior and must not create intermediate Structural groups. General authority shared by multiple Tools remains in the `TOOLS` scope, while authority specific to one Tool belongs to that Tool's scope. A flow may compose peer Tools without introducing an `OPS_TOOLS` group or another structural wrapper.
