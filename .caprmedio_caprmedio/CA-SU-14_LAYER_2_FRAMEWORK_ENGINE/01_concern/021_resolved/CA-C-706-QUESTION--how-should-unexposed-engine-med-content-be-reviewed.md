---
identity:
  id: CA-C-706
  ref_id: CA-C-706
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Resolved
  version: 2
  updated_at: 2026-11-09 07:45:53 +0400
destination:
  file:
    name: CA-C-706-QUESTION--how-should-unexposed-engine-med-content-be-reviewed.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/021_resolved
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-P-2768
  - CA-P-2767
---

## Summary

How should unexposed Engine MED Content be reviewed?

## Question

Should the additional 35 Current MED Atoms with no query-exposed Content be migrated after declared legacy Content is made readable, or be retired after a separate source review?

## Details

Resolved by carrier repair, not retirement. All 35 additional sources were copied into new canonically formatted Drafts without changing their meaning or Current files. Workbench exposed all 35 through query_run; the owning-Scope reviewers then reviewed their actual Claims, corrected the Drafts and rechecked the fixes. Adoption is recorded in the Epic's Work Report and thin index.

The prior 78-RMEDO deferral remains unchanged, including 75 MED Atoms: 64 PROGRAMMATIC and 11 APPS. Those sources and their existing Drafts remain untouched. No reader or runtime code was changed by this specification Epic.
