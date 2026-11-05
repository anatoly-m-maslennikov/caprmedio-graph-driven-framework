---
atom_id: CA-M-476
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
status: Archived
version: 1
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Workspace
relations:
  method_for:
  - CA-R-2902
  - CA-R-2903
carrier_destination:
  file:
    name: CA-M-476@1-CODEX_EXTENSION-ENG_DECISION--coordinate-workbench-workspace-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/05_method/archive
updated_at: 2026-11-05 16:45:35 +0400
---

## Summary

Coordinate Workbench Workspace Views

## Claim

Use the existing native Codex chat as the Workspace boundary. Keep one Workspace per native chat and keep its Views isolated from every other chat and Project.

Implement View operations as small adapters over the existing query executor, pagination, successful-run saving, saved Journal and browser autosave. Keep the caller's order; do not add a magic Workflow or a new scheduler. Return Run metadata first and fetch result rows only when requested.

Keep the query log separate from saved Views. Record only the approved SQL, outcome, error and counts, retain it for seven days, and expire old entries when the log is read. Do not store rows, duplicate schema data or add a cleanup daemon.
