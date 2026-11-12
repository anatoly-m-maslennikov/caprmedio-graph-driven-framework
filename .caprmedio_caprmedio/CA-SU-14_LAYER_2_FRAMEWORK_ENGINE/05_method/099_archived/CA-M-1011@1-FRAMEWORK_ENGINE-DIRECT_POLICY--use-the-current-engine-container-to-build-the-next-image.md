---
identity:
  atom_id: CA-M-1011
  ref_id: CA-M-1011@1
context:
  role: method
  form: direct_policy
  tier: 3
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: archived
  updated_at: '2026-11-12T09:11:13.653926+00:00'
destination:
  file:
    name: CA-M-1011@1-FRAMEWORK_ENGINE-DIRECT_POLICY--use-the-current-engine-container-to-build-the-next-image.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method/099_archived
---
## Summary

Use the current Engine container to build the next image

## Claim

### Prose Claim

Use the current ready Engine container's image to run the Engine steps that build the next image. Give those steps the new build's staged sources. Use the staged sources directly for the first build, when there is no predecessor image.
