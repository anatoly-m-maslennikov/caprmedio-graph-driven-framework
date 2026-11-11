---
identity:
  id: CA-C-730
  ref_id: CA-C-730@14
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
  version: 14
  updated_at: 2026-11-11 14:43:52 +0400
destination:
  file:
    name: CA-C-730@14-QUESTION--admit-the-atom-lifecycle-tool-contract.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/archive
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-P-2934
  - CA-R-1093
  - CA-M-374
  - CA-D-623
  - CA-R-1432
  - CA-R-1788
  - CA-E-521
  - CA-O-10009
  - CA-O-10011
  - CA-O-10016
  - CA-O-10018
  - CA-O-10023
  - CA-O-10024
---

## Summary

Admit the Atom Lifecycle Tool contract

## Concern

What remains to admit and publish the six Atom Lifecycle Tools selected for CA-P-2934?

## Details

The six Workflows and supporting Atoms are Current. The Operator chose direct calls to the Project runtime over MCP. Success returns only operation Status. Git integration is deferred. For missing input, return the requested fields. A later call in the same Project, client session and Tool can supply only those fields and optionally correct others.

A disposable Project passed all six paths through MCP HTTP, including a correction-only call and an Update that preserved Current Status across a Scope Unit change. Local release and direct image builds compile model assets at build time. See CA-P-2977.

Before public registration, complete the model checks under CA-O-10002. The current validator covers exact Status, declared Role literals, explicit Form constraints, supported Header types and duplicate declared Content headings. Required Content and the full qualified Form rules need further work.

For folder-backed parents, CA-R-1521 requires separate actions for latest descendants and preserves older archives. CA-D-664 requires the stored destination to match the actual location. If a parent move carries an older archive whose stored path would change, which rule controls? CA-D-461 also leaves the Done and Canceled placement for Plans with no containing Atom undecided. Keep those writes unavailable until the Carrier rules are settled.
