---
identity:
  atom_id: CA-C-734
  ref_id: CA-C-734@1
context:
  role: concern
  form: Question
  tier: 3
  concern:
    priority: Medium
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: archived
  updated_at: '2026-11-12T03:17:17.749196+00:00'
destination:
  file:
    name: CA-C-734@1-FRAMEWORK_ENGINE-QUESTION--how-should-update-report-corrected-input-after-writing.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/099_archived
---
## Summary

How should Update report corrected input after writing

## Question

If promotion requests corrected input after Update has already saved a Draft and archived the Current Atom, should Update stop and report the error with completed effects, or wait for an explicit correction and resume only promotion?

## Details

CA-O-10024@3 describes waiting and resuming promotion. The current Tool returns failure with completed effects. The decision affects only a correction requested after a write. CA-O-10018@2 already reports failure with completed effects. Tracked in CA-P-2791.
