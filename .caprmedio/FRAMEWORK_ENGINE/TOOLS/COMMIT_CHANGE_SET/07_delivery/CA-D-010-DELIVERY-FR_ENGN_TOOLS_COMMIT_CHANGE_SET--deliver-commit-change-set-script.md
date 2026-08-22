---
subject_scopes:
  - provenance
version: 9
updated_at: 2026-08-22 03:09:20
relations:
  delivery_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-602--use-a-common-tool-cli-interface
---
# Deliver the commit-change-set script

Realize `COMMIT_CHANGE_SET` through the canonical source script `FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET/commit_change_set.py` and its content-identical carrier in the selected `.caprmedio_install` release. It must expose the common Doer CLI contract with dry-run and apply modes, and compose only peer code installed in that release. The interface accepts either a `COMMIT_TRIGGER` for the complete orchestrated flow or a sealed context with the complete receipt set and live lease for the final commit or idempotent retry boundary. It stages an ordinary file, Atom file, or complete folder action as one subject boundary plus all related Journal sidecars. Exact staged and committed path verification disables Git rename detection so a `MOVE` or `MOVE+UPDATE` remains the sealed before-path and after-path action rather than a heuristic Git presentation.

The installed script must also expose `git-hook pre-commit`, `git-hook commit-msg`, and `git-hook post-commit` Evaluation modes. Thin executable carriers under `.caprmedio_install/hooks/git` invoke these modes through the selected content-addressed release. Git registers that directory through repository-local `core.hooksPath`; pre-existing executable hooks in the repository's default `.git/hooks` directory are invoked first and remain byte-for-byte untouched. The pre-commit mode rejects staged installation, runtime, and Git-internal paths before classifying the remaining boundary through canonical Artifact authority.

The post-commit mode writes observation evidence only below `.caprmedio_runtime/logs/git_hooks`, partitioned by the repository host's current local calendar date as NDJSON. Each record binds the commit, parent, changed paths, governed classification, validation result, action identity and completed event identity when applicable, and ordered diagnostics. Its deterministic observation identity makes repeated observation of the same commit idempotent without editing or duplicating an accepted record.
