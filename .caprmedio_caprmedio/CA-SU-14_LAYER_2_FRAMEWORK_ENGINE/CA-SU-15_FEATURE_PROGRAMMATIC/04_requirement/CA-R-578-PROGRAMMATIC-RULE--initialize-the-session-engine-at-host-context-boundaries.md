---
atom_id: CA-R-578
ref_id: CA-R-578
container:
  scope_unit: CA-SU-15
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
tier: 1
relations: {}
status: Active
version: 13
updated_at: 2026-11-10 20:47:54 +0400
subject_scopes:
- session-engine
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
destination:
  file:
    name: CA-R-578-PROGRAMMATIC-RULE--initialize-the-session-engine-at-host-context-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
---
## Summary

Initialize the session engine at host context boundaries

## Claim

### Prose Claim

Each supported agent-host adapter **must** initialize the CAPRMEDIO session engine at the host's session-start **and** post-compaction boundaries **without** requiring `/ca` invocation.

