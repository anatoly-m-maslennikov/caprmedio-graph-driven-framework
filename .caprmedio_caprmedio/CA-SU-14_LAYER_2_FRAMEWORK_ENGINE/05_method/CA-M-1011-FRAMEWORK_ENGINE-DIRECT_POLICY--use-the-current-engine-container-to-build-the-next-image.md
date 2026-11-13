---
identity:
  atom_id: CA-M-1011
  ref_id: CA-M-1011
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
  version: 3
  status: active
  updated_at: '2026-11-12T12:32:38.883300+00:00'
destination:
  file:
    name: CA-M-1011-FRAMEWORK_ENGINE-DIRECT_POLICY--use-the-current-engine-container-to-build-the-next-image.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method
---
## Summary

Use the current Engine container to build the next image

## Claim

### Prose Claim

When refreshing declaration-derived build assets, use the current ready Engine container's image to query the new checkout's staged sources through Workbench. Select eligible Current Declarations by Role and declared main Subject, using their Formal Claims as the source. Do not hardcode Declaration Atom IDs. Use the staged sources directly for the first refresh, when no predecessor image has been recorded.

## Semantics

N+1 applies to asset refresh. A build from the existing asset files uses the selected checkout and needs no CAPRMEDIO runtime or predecessor image.
