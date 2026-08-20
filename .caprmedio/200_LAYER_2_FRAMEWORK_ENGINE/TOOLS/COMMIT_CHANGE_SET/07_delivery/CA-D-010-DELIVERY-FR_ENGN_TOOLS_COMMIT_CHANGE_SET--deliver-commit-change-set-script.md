---
subject_scopes:
  - provenance
version: 3
updated_at: 2026-08-21 01:33:02
relations:
  delivery_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-602--use-a-common-tool-cli-interface
---
# Deliver the commit-change-set script

Realize `COMMIT_CHANGE_SET` through the canonical source script `.caprmedio/200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET/commit_change_set.py` and its content-identical installed runtime carrier. It must expose the common Doer CLI contract with dry-run and apply modes, and compose only peer code installed in the same runtime release. The interface accepts either a `COMMIT_TRIGGER` for the complete orchestrated flow or a sealed context with the complete receipt set and live lease for the final commit or idempotent retry boundary.

The installed script must also expose `git-hook pre-commit`, `git-hook commit-msg`, and `git-hook post-commit` Evaluation modes. Thin executable carriers under `.caprmedio_runtime/hooks/git` invoke these modes through the current content-addressed release. Git registers that directory through repository-local `core.hooksPath`; pre-existing executable hooks in the repository's default `.git/hooks` directory are invoked first and remain byte-for-byte untouched. The post-commit mode writes observation evidence only below `.caprmedio_runtime/logs/git_hooks`.
