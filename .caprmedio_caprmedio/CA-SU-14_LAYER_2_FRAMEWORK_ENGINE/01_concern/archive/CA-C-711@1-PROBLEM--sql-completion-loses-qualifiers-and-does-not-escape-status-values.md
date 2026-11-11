---
identity:
  id: CA-C-711
  ref_id: CA-C-711@1
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Problem
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Archived
  version: 1
  updated_at: 2026-11-09 07:55:38 +0400
destination:
  file:
    name: CA-C-711@1-PROBLEM--sql-completion-loses-qualifiers-and-does-not-escape-status-values.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/archive
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-M-468
  - CA-I-8
---

## Summary

SQL completion loses qualifiers and does not escape status values

## Concern

SqlEditor.svelte replaces the typed qualified token using only its quoted column name, and status-value completion does not double embedded apostrophes. Keep M468 unchanged and fix these implementation defects in the follow-up Epic. Verify both through the editor.
