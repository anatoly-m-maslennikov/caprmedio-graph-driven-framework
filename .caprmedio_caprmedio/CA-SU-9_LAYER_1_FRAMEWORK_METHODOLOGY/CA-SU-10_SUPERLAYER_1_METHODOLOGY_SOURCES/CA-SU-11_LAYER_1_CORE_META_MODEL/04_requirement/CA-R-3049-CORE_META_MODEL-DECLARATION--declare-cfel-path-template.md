---
identity:
  id: CA-R-3049
  ref_id: CA-R-3049
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ CFEL/Function//PATH_TEMPLATE
  tier: 3
state:
  status: active
  version: 5
  updated_at: '2026-11-11T19:37:42+04:00'
destination:
  file:
    name: CA-R-3049-CORE_META_MODEL-DECLARATION--declare-cfel-path-template.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare CFEL PATH_TEMPLATE

## Claim

### Prose Claim

`PATH_TEMPLATE([string])` returns one repository-relative directory path for the selected Atom. Its argument is a quoted template. A named component occupies a complete segment.

- `<owning scope unit>` resolves to the owning Scope Unit directory.
- `<role folder>` resolves to the selected Role folder derived under CA-D-296.
- `<container>` resolves to the Scope Unit's Role directory or the containing Atom's matching Directory Carrier.
- `<status folder>` resolves to the Status folder name derived under CA-D-717.
- `<placement>` resolves to the directory suffix selected by the applicable Status rule. Omit that segment when the suffix is empty.

A Role template combines the derived Role folder with the applicable Status placement. Resolve that Status template before substituting `<placement>`. A specific Status rule takes precedence over the Status Group rule. A Role-qualified Status rule takes precedence over the same Status rule without a Role. The resolved path contains no unresolved components, absolute prefix or parent-directory traversal.
