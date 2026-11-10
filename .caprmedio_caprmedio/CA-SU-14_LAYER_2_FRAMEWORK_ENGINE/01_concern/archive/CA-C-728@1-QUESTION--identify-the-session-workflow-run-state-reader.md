---
identity:
  id: CA-C-728
  ref_id: CA-C-728@1
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Archived
  version: 1
  updated_at: 2026-11-11 00:22:28 +0400
destination:
  file:
    name: CA-C-728@1-QUESTION--identify-the-session-workflow-run-state-reader.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/archive
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-R-3016
  - CA-M-517
---

## Summary

Identify the session Workflow Run state reader

## Concern

R3016 requires Project/session-isolated active Run lists and recorded history. The installed provider inventory is Workbench-only, and initial PROGRAMMATIC inspection found no retained generic executor or Run-state reader. The legacy Journal library writes records but supplies no generic reader; release events currently use Run IDs as session IDs and cannot establish client-session ownership.

Do not invent an empty successful result or a parallel Run store. Identify an admitted state/history owner, or explicitly defer the read capability while implementing the independent generic caller context and hook. The Operator question is pending; broad source investigation continues.
