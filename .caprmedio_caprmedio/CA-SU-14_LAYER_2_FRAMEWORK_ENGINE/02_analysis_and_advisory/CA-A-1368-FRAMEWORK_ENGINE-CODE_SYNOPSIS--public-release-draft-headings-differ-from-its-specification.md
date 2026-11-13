---
identity:
  atom_id: CA-A-1368
  ref_id: CA-A-1368
context:
  role: analysis_and_advisory
  form: code_synopsis
  tier: 4
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:54:03.059032+00:00'
destination:
  file:
    name: CA-A-1368-FRAMEWORK_ENGINE-CODE_SYNOPSIS--public-release-draft-headings-differ-from-its-specification.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Public Release draft headings differ from its specification

## Claim

### Prose Claim

CA-M-366@19 and CA-E-612@18 name `What's new` and `What's fixed` as separate sections. `LAYER_5_FRAMEWORK_DELIVERY/PUBLIC_RELEASE/public_release_materials.py` requires `## New` and `## Fixed`. A draft that uses the documented labels fails validation.
