---
subject_scopes:
  - feature-boundary
version: 1
updated_at: 2026-08-20 19:15:57
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-702--define-tools-feature-scope
---
# Define the OPS_TOOLS Feature group

`OPS_TOOLS` must be one unordered structural group owned immediately by `TOOLS`, addressed by `FRAMEWORK_ENGINE/TOOLS/OPS_TOOLS`, and realized under `02_FR_ENGN/TOOLS/OPS_TOOLS/`. It owns operational entry hooks and the Finders and Doers they trigger for repository lifecycle actions; hooks only emit triggers, Finders remain read-only, and Doers own mutations.
