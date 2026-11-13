---
identity:
  atom_id: CA-A-1364
  ref_id: CA-A-1364
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
  updated_at: '2026-11-12T12:53:48.079601+00:00'
destination:
  file:
    name: CA-A-1364-FRAMEWORK_ENGINE-CODE_SYNOPSIS--stdio-saved-query-responses-omit-the-url.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Stdio saved query responses omit the URL

## Claim

### Prose Claim

CA-D-673@18 requires a saved query ID and URL. CA-M-1008@1 provides equivalent Tool behavior through HTTP and stdio. `FEATURE_MCP/registry_workbench_provider.py` presents a URL only when an HTTP request is available. `FEATURE_MCP/workbench_links.py` derives its base from that request. The stdio path returns the ID without the required URL.
