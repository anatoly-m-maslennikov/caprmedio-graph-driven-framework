---
identity:
  atom_id: CA-A-1375
  ref_id: CA-A-1375
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
  updated_at: '2026-11-12T12:59:09.995903+00:00'
destination:
  file:
    name: CA-A-1375-FRAMEWORK_ENGINE-CODE_SYNOPSIS--local-release-packages-less-than-the-specified-engine-tree.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Local Release packages less than the specified Engine tree

## Claim

### Prose Claim

CA-D-562@25 names the complete Engine tree as the runtime package source. `LAYER_5_FRAMEWORK_DELIVERY/RELEASE_VERSION/release_support.py` packages the Programmatic subtree and the canonical Skill, excluding selected source and test carriers. The package can omit Engine files named by the Delivery scope. The reviewed checkout separately defers several Engine areas, so the correct package boundary needs a spec decision.
