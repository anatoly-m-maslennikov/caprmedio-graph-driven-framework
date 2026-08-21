---
atom_id: CA-M-103
subject_scopes:
  - feature-boundary
version: 3
updated_at: 2026-08-21 04:52:02
relations:
  method_for:
    - CA-R-856
---
# Install one verified Tool release

Inventory every eligible regular file below the canonical Tool source, excluding tests, caches, bytecode, and host metadata; bind its relative path, content digest, and executable mode into one release digest; stage the complete release; verify its manifest and every copied byte; then atomically select it through `.caprmedio_install/current.toml`.

After selection, register the enabled Codex adapter; merge wildcard `PreToolUse` and `PostToolUse` plus `SessionStart` and `Stop` dispatcher groups into the user-level Codex Hook carrier; register Git `pre-commit`, `commit-msg`, and `post-commit` Hooks; and install stable Tool launchers. Each generic Codex command resolves the current Git root, exits without effect when the repository lacks an executable `.caprmedio_install/bin/commit-trigger`, and otherwise delegates to that launcher. Remove recognized managed groups from the former project-local Codex carrier without changing unrelated project groups. Reinstallation reuses an identical release or selects a new digest, rewrites the launcher behind its stable address, and preserves the generic Codex Hook definition byte-for-byte when its behavior contract is unchanged. Report Codex host activation as operator-reviewed external state rather than infer it from carrier presence. Remove only recognized obsolete CAPRMEDIO installation and Hook directories from `.caprmedio_runtime` after the new installation verifies.
