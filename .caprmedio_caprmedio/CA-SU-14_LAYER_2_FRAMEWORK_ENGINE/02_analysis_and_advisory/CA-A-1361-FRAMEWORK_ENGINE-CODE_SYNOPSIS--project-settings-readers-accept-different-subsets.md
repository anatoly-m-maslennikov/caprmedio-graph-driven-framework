---
identity:
  atom_id: CA-A-1361
  ref_id: CA-A-1361
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
  updated_at: '2026-11-12T12:53:38.937312+00:00'
destination:
  file:
    name: CA-A-1361-FRAMEWORK_ENGINE-CODE_SYNOPSIS--project-settings-readers-accept-different-subsets.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Project Settings readers accept different subsets

## Claim

### Prose Claim

CA-M-284@31 requires one complete validated immutable Project Settings snapshot. `FEATURE_TOOLS/project_selection.py` validates the Project name and paths, `project_settings_values.py` can read a fallback directly, and `compile_applicable_methodology.py` performs a separate TOML read on the release path. The complete schema parser has no production caller. The same Settings can therefore receive different checks across components.
