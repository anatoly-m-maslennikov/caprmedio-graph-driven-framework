---
identity:
  id: CA-D-716
  ref_id: CA-D-716@3
context:
  container:
    scope_unit: CA-SU-11
  role: delivery
  form: file_layout
  topics:
    main_subject: 'CAPRMEDIO_MODEL <+ Atom.Header.State.Status >| Status Group := Draft'
    dependencies:
    - CAPRMEDIO_MODEL <+ Carrier
  tier: 3
state:
  status: archived
  version: 3
  updated_at: '2026-11-11T19:06:04+04:00'
destination:
  file:
    name: CA-D-716@3-CORE_META_MODEL-FILE_LAYOUT--place-draft-atom-carriers-in-the-owning-role-folder.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/099_archived
---

## Summary

Place Draft Atom Carriers in the owning Role folder

## Claim

### Prose Claim

Place Draft Atom Markdown Carriers in the shared `<owning scope unit>/<role folder>/000_draft/` directory. The Atom's owning Scope Unit and Role determine this directory.

For example, Draft Plans use `<scope unit>/03_plan/000_draft/`.

### Formal Claim

```CFEL
# model
Atom/(.Header.State.Status := Draft).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/000_draft");
```
