---
subject_scopes:
  - feature-boundary
version: 6
updated_at: 2026-08-21 04:24:00
relations:
  delivery_for:
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_TRIGGER--emit-only-operational-hook-triggers
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-602--use-a-common-tool-cli-interface
---
# Deliver the commit-trigger script

Realize `COMMIT_TRIGGER` through the canonical source script `102_FRAMEWORK_ENGINE/TOOLS/COMMIT_TRIGGER/commit_trigger.py` and its content-identical carrier in the selected `.caprmedio_install` release. `INSTALL_TOOLS`, not `COMMIT_TRIGGER`, owns Tool and Hook installation. `COMMIT_TRIGGER` exposes the common Hook CLI contract, implements registered Hook adapters without embedding substrate-specific meaning into the canonical trigger, and hands an accepted trigger unchanged to the `COMMIT_CHANGE_SET` end-to-end interface.

The Codex host carrier invokes the stable install-owned `commit-trigger` launcher, which resolves only the release selected by `.caprmedio_install/current.toml`. Its command identity does not contain a release digest. Its before-event callback may write one reconstructible runtime frontier snapshot keyed by the Codex session and tool-use identities; its matching after-event callback consumes and removes that snapshot, emits the canonical trigger without semantic classification, passes the unchanged trigger to `COMMIT_CHANGE_SET`, and records only reconstructible runtime completion or failure diagnostics. These host-transport effects do not alter the trigger, establish governed meaning, or give `COMMIT_TRIGGER` ownership of context gathering, Journal append, commit, or installation semantics.

Adapter installation and removal must preserve pre-existing repository Hook behavior. Installation must refuse a different pre-existing local `core.hooksPath` with a stable diagnostic and zero configuration or Hook-carrier mutation. When no conflicting path exists, it registers the managed installation Hook directory and chains any executable default `.git/hooks` carrier before the managed Evaluation.
