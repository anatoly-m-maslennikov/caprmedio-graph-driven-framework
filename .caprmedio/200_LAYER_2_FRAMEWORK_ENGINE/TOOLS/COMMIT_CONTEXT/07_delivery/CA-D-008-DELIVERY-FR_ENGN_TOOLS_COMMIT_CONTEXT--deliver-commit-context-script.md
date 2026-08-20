---
subject_scopes:
  - feature-boundary
version: 1
updated_at: 2026-08-20 23:35:00
relations:
  delivery_for:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-602--use-a-common-tool-cli-interface
---
# Deliver the commit-context script

Realize `COMMIT_CONTEXT` through the one canonical independently executable script `02_FR_ENGN/TOOLS/COMMIT_CONTEXT/commit_context.py`. It must expose the common read-only Finder CLI contract. The standalone script and the logic invoked by `COMMIT_CHANGE_SET` must call the same non-executable implementation and return the same sealed context for the same trigger and unchanged source frontier.
