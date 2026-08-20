---
subject_scopes:
  - feature-boundary
version: 2
updated_at: 2026-08-21 01:09:53
relations:
  delivery_for:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-602--use-a-common-tool-cli-interface
---
# Deliver the commit-context script

Realize `COMMIT_CONTEXT` through the canonical source script `.caprmedio/200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/COMMIT_CONTEXT/commit_context.py` and its content-identical installed runtime carrier. It must expose the common read-only Finder CLI contract. The standalone script and the logic invoked by `COMMIT_CHANGE_SET` must call the same runtime-local non-executable implementation and return the same sealed context for the same trigger and unchanged source frontier.
