---
identity:
  id: CA-C-731
  ref_id: CA-C-731
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Question
  concern:
    priority: Medium
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 19:26:12 +0400
destination:
  file:
    name: CA-C-731-FRAMEWORK_ENGINE-QUESTION--admit-work-sequence-plan-filenames-in-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern
relations:
  concern_about:
  - CA-D-469
  - CA-C-717
author: Anatoly Maslennikov
---

## Summary

Admit Work Sequence Plan filenames in Workbench

## Concern

Should Workbench accept a Plan filename with its declared Work Sequence Number before the Project-prefixed Atom ID?

## Details

Current CA-D-469 allows this filename order. Workbench still requires the Project prefix at the start of the filename before it reads the Header. The native 001_backlog folders contain 50 Plans. Live query_run shows the 11 whose filenames start with the Atom ID and omits the 39 whose filenames start with a Work Sequence Number. Changing the Plan filename selection would make these Plans queryable without moving or renaming their carriers.
