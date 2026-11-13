---
identity:
  atom_id: CA-A-1366
  ref_id: CA-A-1366
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
  updated_at: '2026-11-12T12:53:54.673561+00:00'
destination:
  file:
    name: CA-A-1366-FRAMEWORK_ENGINE-CODE_SYNOPSIS--local-release-can-clean-images-after-focused-checks.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Local Release can clean images after focused checks

## Claim

### Prose Claim

CA-M-332@24 permits Local Release after green selected-module checks. CA-D-564@19 and CA-D-562@25 require a green full suite for cleanup or installation. `LAYER_5_FRAMEWORK_DELIVERY/RELEASE_VERSION/local_release.py` runs the same install and image cleanup after the focused and full paths. The code follows the Method and exposes a disagreement with the Delivery contracts.
