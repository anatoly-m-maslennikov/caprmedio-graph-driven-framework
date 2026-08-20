---
subject_scopes:
  - provenance
version: 2
updated_at: 2026-08-21 01:09:53
relations:
  delivery_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-602--use-a-common-tool-cli-interface
---
# Deliver the commit-change-set script

Realize `COMMIT_CHANGE_SET` through the canonical source script `.caprmedio/200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET/commit_change_set.py` and its content-identical installed runtime carrier. It must expose the common Doer CLI contract with dry-run and apply modes, and compose only peer code installed in the same runtime release. The interface accepts either a `COMMIT_TRIGGER` for the complete orchestrated flow or a sealed context with the complete receipt set and live lease for the final commit or idempotent retry boundary.
