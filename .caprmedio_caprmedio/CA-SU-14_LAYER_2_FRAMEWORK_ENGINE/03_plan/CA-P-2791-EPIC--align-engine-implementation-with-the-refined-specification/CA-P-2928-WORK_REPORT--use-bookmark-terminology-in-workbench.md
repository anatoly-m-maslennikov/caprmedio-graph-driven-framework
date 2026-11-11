---
identity:
  id: CA-P-2928
  ref_id: CA-P-2928
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-11 03:14:33 +0400
destination:
  file:
    name: CA-P-2928-WORK_REPORT--use-bookmark-terminology-in-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2852
author: Anatoly Maslennikov
---

## Summary

Use Bookmark terminology in Workbench

## Details

Reviewed R2776@9, D673@18 and M516@2. Result-file formats already passed live acceptance in P2923. Fixed the remaining frontend terminology: permanent query entries now display Bookmark; named-save and open dialogs distinguish Bookmarks from saved Views. Kept storage kinds, tool names, IDs, URLs and Run & Save behavior unchanged.

Production standalone and MCP App frontend builds passed, with existing Svelte initial-prop and bundle-size warnings. Three saved-item compatibility tests passed. Two browser tests passed against the rebuilt local frontend and the live image's backend, including actual Bookmark listing, saved-View identity reuse and independent duplication. The first run exposed missing saved-list/load routes in the temporary test proxy; correcting that proxy required no product logic change. The temporary frontend server was stopped.

These labels are prepared in source and built assets, not deployed in the retained image yet. P2852 is Active pending final image acceptance and complete result-delivery/Bookmark checklist reconciliation. Evidence: .caprmedio_tmp/CA-P-2791/CA-P-2852/frontend-bookmark-build.log, saved-items-tests.log and bookmark-browser-after-proxy.log.
