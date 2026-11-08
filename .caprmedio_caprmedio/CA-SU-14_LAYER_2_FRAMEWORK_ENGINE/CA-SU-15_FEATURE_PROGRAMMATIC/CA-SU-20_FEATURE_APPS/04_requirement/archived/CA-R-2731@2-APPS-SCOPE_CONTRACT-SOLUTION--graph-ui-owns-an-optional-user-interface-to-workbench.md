---
identity:
  atom_id: CA-R-2731
  ref_id: CA-R-2731@2
context:
  container:
    scope_unit: CA-SU-20
  role: Requirement
  form: Solution
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Aspect/UX
    - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  tier: 0
state:
  status: Archived
  version: 2
  updated_at: 2026-11-09 00:09:26 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
claim_target_scope_unit: GRAPH_UI
destination:
  file:
    name: CA-R-2731@2-APPS-SCOPE_CONTRACT-SOLUTION--graph-ui-owns-an-optional-user-interface-to-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/archived
---
## Summary

GRAPH_UI owns an optional user interface to WORKBENCH

## Claim

GRAPH_UI **must** own the optional human-facing interface over WORKBENCH. GRAPH_UI **must not** be a prerequisite for **any** of the following:

- headless graph access;
- Tools; **or**
- MCP.
