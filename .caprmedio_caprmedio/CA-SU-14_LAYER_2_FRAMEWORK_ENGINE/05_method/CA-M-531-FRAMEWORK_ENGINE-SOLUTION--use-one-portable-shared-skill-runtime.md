---
atom_id: CA-M-531
ref_id: CA-M-531
container:
  scope_unit: CA-SU-14
role: Method
form: Solution
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Component Structure
tier: 1
relations:
  child_of:
  - CA-M-261
  IS_REPLACEMENT_FOR:
  - CA-R-564
status: Active
version: 1
updated_at: 2026-11-10 20:47:54 +0400
subject_scopes:
- runtime
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: FRAMEWORK_ENGINE
destination:
  file:
    name: CA-M-531-FRAMEWORK_ENGINE-SOLUTION--use-one-portable-shared-skill-runtime.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method
---
## Summary

Use one portable shared Skill runtime

## Claim



### Prose Claim
**all** CAPRMEDIO Skills for one agent host invoke one versioned portable shared runtime that deterministically resolves the owning project, project-local governance, routing, **and** required session **or** Journal setup; thin wrappers duplicate no shared mechanics **and** fail closed **when** the runtime boundary cannot be resolved.
