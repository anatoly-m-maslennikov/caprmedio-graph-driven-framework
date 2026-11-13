---
identity:
  atom_id: CA-A-1352
  ref_id: CA-A-1352
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
  updated_at: '2026-11-12T12:49:20.652981+00:00'
destination:
  file:
    name: CA-A-1352-FRAMEWORK_ENGINE-CODE_SYNOPSIS--engine-replacements-stage-beneath-the-runtime-directory.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Engine replacements stage beneath the runtime directory

## Claim

### Prose Claim

In the CAPRMEDIO working tree based on `c0b983cb27`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/project_mcp_bootstrap.py`, `deploy_project_mcp_bootstrap`, stages replacement bootstrap files under `.caprmedio_runtime`. `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py`, `stage_outputs`, also puts replacement staging beneath `.caprmedio_runtime`. Both are used by Local Release. CA-M-422@13 requires atomic replacement staging under Project `.caprmedio_tmp` with a same-filesystem check. These paths use a different staging location.
