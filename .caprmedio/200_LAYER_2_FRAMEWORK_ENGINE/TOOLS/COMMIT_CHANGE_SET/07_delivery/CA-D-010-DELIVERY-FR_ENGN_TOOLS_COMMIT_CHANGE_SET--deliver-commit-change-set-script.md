---
subject_scopes:
  - provenance
version: 1
updated_at: 2026-08-20 23:37:00
relations:
  delivery_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-602--use-a-common-tool-cli-interface
---
# Deliver the commit-change-set script

Realize `COMMIT_CHANGE_SET` through the one canonical independently executable script `02_FR_ENGN/TOOLS/COMMIT_CHANGE_SET/commit_change_set.py`. It must expose the common Doer CLI contract with dry-run and apply modes. The interface accepts either a `COMMIT_TRIGGER` for the complete orchestrated flow or a sealed context with the complete receipt set and live lease for the final commit or idempotent retry boundary.
