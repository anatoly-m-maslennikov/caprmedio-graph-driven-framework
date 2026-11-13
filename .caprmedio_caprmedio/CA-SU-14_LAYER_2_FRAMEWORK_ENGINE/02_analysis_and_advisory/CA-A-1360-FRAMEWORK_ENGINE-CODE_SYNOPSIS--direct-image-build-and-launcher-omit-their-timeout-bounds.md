---
identity:
  atom_id: CA-A-1360
  ref_id: CA-A-1360
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
  updated_at: '2026-11-12T12:53:36.316167+00:00'
destination:
  file:
    name: CA-A-1360-FRAMEWORK_ENGINE-CODE_SYNOPSIS--direct-image-build-and-launcher-omit-their-timeout-bounds.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Direct image build and launcher omit their timeout bounds

## Claim

### Prose Claim

CA-M-409@14 requires bounded external execution. The direct build CLI accepts `--build-timeout` but does not pass it to its build call. `FEATURE_MCP/docker/start_mcp.py` also launches its outer `uv run` subprocess without a deadline, even though inner operations have bounds.
