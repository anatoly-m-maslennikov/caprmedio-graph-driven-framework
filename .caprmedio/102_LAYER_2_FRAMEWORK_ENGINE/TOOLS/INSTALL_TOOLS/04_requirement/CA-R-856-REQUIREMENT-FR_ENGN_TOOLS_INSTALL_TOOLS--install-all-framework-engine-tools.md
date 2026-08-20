---
atom_id: CA-R-856
subject_scopes:
  - feature-boundary
version: 2
updated_at: 2026-08-21 04:23:00
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-702--define-tools-feature-scope
---
# Install all Framework Engine Tools

`INSTALL_TOOLS` must be one Doer Tool owned immediately by `TOOLS` as an `unordered_unit` at Structural level `3`, addressed by `FRAMEWORK_ENGINE/TOOLS/INSTALL_TOOLS`, and realized under `102_FRAMEWORK_ENGINE/TOOLS/INSTALL_TOOLS/`. It must resolve every runnable Tool and shared implementation dependency from the canonical root `102_FRAMEWORK_ENGINE/TOOLS`, publish one digest-verified content-addressed release under `.caprmedio_install`, select that release through one machine-readable current manifest, and install every registered stable launcher and host Hook for the selected release. Host Hook commands must address stable install-owned launchers rather than content-addressed release paths so selecting a new release does not change a previously reviewed Hook identity.

Installation must use dry-run unless apply is explicit, preserve pre-existing default Hook behavior, reject an unrelated local `core.hooksPath` before mutation, migrate only recognized prior CAPRMEDIO installation carriers, and leave mutable execution state under `.caprmedio_runtime`. Installed Tools must remain runnable when the canonical source is not on their import path and must not create bytecode, logs, caches, PIDs, or mutable state below `.caprmedio_install`. Installation status must distinguish an installed Hook carrier from host activation and must state when the host requires one operator-controlled trust or review action that the installer cannot establish.
