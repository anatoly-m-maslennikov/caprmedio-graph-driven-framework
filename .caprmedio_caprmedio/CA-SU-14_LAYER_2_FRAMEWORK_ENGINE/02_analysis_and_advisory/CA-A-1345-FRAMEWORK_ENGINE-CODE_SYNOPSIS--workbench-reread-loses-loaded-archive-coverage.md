---
identity:
  atom_id: CA-A-1345
  ref_id: CA-A-1345
context:
  role: analysis_and_advisory
  form: code_synopsis
  tier: 4
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:48:48.271451+00:00'
destination:
  file:
    name: CA-A-1345-FRAMEWORK_ENGINE-CODE_SYNOPSIS--workbench-reread-loses-loaded-archive-coverage.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Workbench reread loses loaded Archive coverage

## Claim

### Prose Claim

In the CAPRMEDIO working tree based on `c0b983cb27`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/workbench_tools.py` replaces the Workbench service in its reread operation. The replacement starts with empty loaded Archive coverage in `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/service.py`. Previously loaded Archived rows therefore disappear after reread until the caller loads the scopes again. CA-R-2786@5 and CA-E-677@30 require reread to retain the selected Archive coverage while rebuilding derived data under the installed schema.
