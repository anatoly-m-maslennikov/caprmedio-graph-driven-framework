---
subjects:
  governs: feature-boundary
  depends_on: []
version: 21
updated_at: 2026-10-23 03:17:34 +0400
relations:
  delivery_for:
  - CA-R-856
  - CA-M-103
  - CA-R-1124
  - CA-R-1064
  - CA-R-1065
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-D-011@21
status: Archived
---
# Deliver the Tool installer

Realize the existing `INSTALL_TOOLS` Tool through `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/INSTALL_TOOLS/install_tools.py` and its shared non-executable `framework_installation.py` library. The Tool exposes machine-readable `describe`, read-only `status`, dry-run `run`, and explicit `run --apply` interfaces. This ordinary managed-Tool installer is not the retired separate Framework-package initialization or native runtime-installation API.

The retained installer inventories the canonical Tool sources, stages and verifies the complete managed Tool release below `.caprmedio_tmp/install_tools/`, and publishes its verified bytes, manifest, stable launchers and current Tool selection below `.caprmedio_runtime/tools/`. Existing source/currentness, path, byte and mode checks and installed inventory/status remain required. The retired reusable Framework package, package/target selectors, state-generation and Full Gate contracts do not govern this ordinary Tool installation.

Persistent configuration and operational state outside the managed Tool surface remain protected. Selected host integrations, recognized legacy migration and failure handling remain governed by CA-R-856 and CA-M-103; `--without-hooks` leaves host Hook integrations unchanged. This retirement alignment grants no new Hook, Git-configuration, user-Carrier or cleanup authority and does not waive those existing preservation/restoration obligations. Plain Journal append/read is independent observation, not a receipt or completion prerequisite, and introduces no `recording_pending` or recording-only retry/recovery operation. Actual installation failures and logging diagnostics remain truthful; no log entry authorizes effect replay.
