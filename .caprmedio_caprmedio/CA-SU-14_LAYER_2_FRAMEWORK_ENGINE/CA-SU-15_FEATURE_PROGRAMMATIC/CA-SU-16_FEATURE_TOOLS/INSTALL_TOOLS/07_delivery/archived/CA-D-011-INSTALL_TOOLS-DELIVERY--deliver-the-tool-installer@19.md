---
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 19
updated_at: 2026-10-09 17:01:07 +0400
relations:
  delivery_for:
    - CA-R-856
    - CA-M-103
    - CA-R-1124
    - CA-R-1064
    - CA-R-1065
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Deliver the Tool installer

Realize the existing `INSTALL_TOOLS` Tool through `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/INSTALL_TOOLS/install_tools.py` and its shared non-executable `framework_installation.py` library. The first-initialization variant delegates through this existing Tool; it does not declare another public Tool. The Tool exposes machine-readable `describe`, read-only `status`, dry-run `run`, and explicit `run --apply` interfaces.

Reusable package content and its manifest are governed only by `102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-596-TOOLS-DELIVERY--encode-the-reusable-framework-package.md`; the sole package selector is governed only by `102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-598-TOOLS-DELIVERY--encode-current-reusable-package-selector.md`; and the target runtime selector is governed only by `102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-599-TOOLS-DELIVERY--encode-target-runtime-installation-selector.md`. This Delivery adds no competing runtime layout, selector or manifest schema. Stable package-owned wrappers and environment follow CA-D-601. Mutable target settings live only at `.caprmedio_runtime/config.toml`: a default is created only when absent, and existing bytes are never overwritten by apply, upgrade, rollback or recovery.

Installation staging and atomic-write intermediates live below `.caprmedio_tmp/release_candidates/<run_id>/`. The Tool does not install Codex or Git Hooks, alter user Carriers or Git configuration, delete `.caprmedio_install/`, or treat legacy runtime state as cleanup authority. Failed pre-activation publication preserves the prior selection; after activation, a missing terminal Journal record is retained as `recording_pending` and only exact terminal-recording recovery is allowed.
