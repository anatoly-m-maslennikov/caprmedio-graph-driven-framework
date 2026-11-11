---
identity:
  id: CA-C-711
  ref_id: CA-C-711
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Problem
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Resolved
  version: 2
  updated_at: 2026-11-11 02:40:22 +0400
destination:
  file:
    name: CA-C-711-PROBLEM--sql-completion-loses-qualifiers-and-does-not-escape-status-values.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/021_resolved
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-M-468
---

## Summary

SQL completion loses qualifiers and does not escape status values

## Concern

SqlEditor.svelte replaces the typed qualified token using only its quoted column name, and status-value completion does not double embedded apostrophes. Keep M468 unchanged and fix these implementation defects in the follow-up Epic. Verify both through the editor.

## Resolution

P2812 corrected qualifier preservation and apostrophe handling. Integration-owner code review and the real-image browser scenario passed; no Run, Check or Save was issued during completion. Historical I8 evidence remains context, not a Current governing link. See P2924.
