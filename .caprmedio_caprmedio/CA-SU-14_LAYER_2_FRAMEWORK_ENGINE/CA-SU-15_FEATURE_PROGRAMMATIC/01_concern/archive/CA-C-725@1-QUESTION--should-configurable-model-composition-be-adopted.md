---
identity:
  atom_id: CA-C-725
  ref_id: CA-C-725@1
context:
  container:
    scope_unit: CA-SU-15
  role: concern
  form: question
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data
      Handling <+ Schema
  tier: 4
state:
  status: Archived
  version: 1
  updated_at: 2026-11-10 15:19:11 +0400
destination:
  file:
    name: CA-C-725@1-QUESTION--should-configurable-model-composition-be-adopted.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/01_concern/archive
relations:
  concern_about:
  - CA-R-1375
---

## Summary

Should configurable model composition be adopted?

## Concern

Four unpromoted Drafts propose a generic model-composition mechanism with additions, overrides and runtime refresh. They still leave the carrier, composition mechanism, refresh trigger, override permissions and invalid-refresh behavior open. Current R1375 forbids Core shadowing or reinterpretation; these Drafts do not supply a new permission.

## Details

Keep the four Drafts unadopted while completing the reviewed Engine specification. Do not turn their open alternatives into runtime requirements or broaden the Workbench schema mechanism to implement them.

A future proposal must choose the permitted extension surface, exact source/configuration format and precedence, and whether rejected refresh pauses model-dependent work or retains the prior complete generation. Then review its Method, Evaluations and Delivery against that choice.

Blast radius: four first-version Drafts only. No Current Atom, Core authority, Scope tree or running service changes.

## Draft sources

- CA-R-2968
- CA-M-494
- CA-E-789
- CA-D-699
