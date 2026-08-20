---
subject_scopes:
  - feature-boundary
tier: core
version: 3
updated_at: 2026-08-20 21:57:00
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-702--define-tools-feature-scope
---
# Define the OPS_TOOLS Feature group

`OPS_TOOLS` must be one unordered structural group owned immediately by `TOOLS`, addressed by `FRAMEWORK_ENGINE/TOOLS/OPS_TOOLS`, and realized under `02_FR_ENGN/TOOLS/OPS_TOOLS/`. It owns operational entry Hooks and the Finders and Doers they trigger for repository changes; Hooks only emit triggers, Finders remain strictly read-only, and Doers own mutations.
