---
subject_scopes:
  - feature-boundary
version: 6
updated_at: 2026-08-21 06:14:03
relations:
  delivery_for:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-602--use-a-common-tool-cli-interface
---
# Deliver the commit-context script

Realize `COMMIT_CONTEXT` through the canonical source script `102_FRAMEWORK_ENGINE/TOOLS/COMMIT_CONTEXT/commit_context.py` and its content-identical carrier in the selected `.caprmedio_install` release. It must expose the common read-only Finder CLI contract. The standalone script and the logic invoked by `COMMIT_CHANGE_SET` must call the same release-local non-executable implementation and return the same sealed context for the same trigger and unchanged source frontier.

The implementation indexes carrier identities tolerantly for relation decoration: an identity collision removes only that ambiguous lookup key, while exact unambiguous filenames remain usable. Relation registry, lifecycle, version, duplicate, missing-target, and ambiguity defects are returned as non-blocking context diagnostics. They never turn this operational logger into a repository-wide graph validator or prevent an otherwise valid file action from reaching the Journal and Git commit boundary.
