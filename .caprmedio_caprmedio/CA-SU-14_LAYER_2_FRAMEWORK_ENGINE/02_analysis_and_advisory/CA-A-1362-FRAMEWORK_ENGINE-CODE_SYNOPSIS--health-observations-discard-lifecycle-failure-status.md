---
identity:
  atom_id: CA-A-1362
  ref_id: CA-A-1362
context:
  role: analysis_and_advisory
  form: code_synopsis
  tier: 4
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:53:42.593828+00:00'
destination:
  file:
    name: CA-A-1362-FRAMEWORK_ENGINE-CODE_SYNOPSIS--health-observations-discard-lifecycle-failure-status.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Health observations discard lifecycle failure status

## Claim

### Prose Claim

CA-R-2446@4 and CA-E-640@15 require truthful Tool health observations. The lifecycle provider returns `status`, while `FEATURE_MCP/health_observations.py` examines `outcome`. A local probe with `status: failed` produced an observation of `returned` with outcome `unknown` and no failure category.
