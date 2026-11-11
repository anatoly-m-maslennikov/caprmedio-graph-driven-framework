---
identity:
  id: CA-D-716
  ref_id: CA-D-716@1
context:
  container:
    scope_unit: CA-SU-11
  role: delivery
  form: decision
  topics:
    main_subject: 'CAPRMEDIO_MODEL <+ Atom.Header.State.Status: Draft'
    dependencies:
    - CAPRMEDIO_MODEL <+ Carrier
  tier: 3
state:
  status: archived
  version: 1
  updated_at: '2026-11-11T17:45:31+04:00'
destination:
  file:
    name: CA-D-716@1-CORE_META_MODEL-DECISION--place-draft-atom-carriers-in-the-owning-role-folder.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/archived
---

## Summary

Place Draft Atom Carriers in the owning Role folder

## Claim

### Prose Claim

Place Draft Atom Markdown Carriers in the shared `<scope unit>/<role number>_<role name lowercase>/draft/` directory. The Atom's owning Scope Unit and Role determine this directory.

For example, Draft Plans use `<scope unit>/03_plan/draft/`.
