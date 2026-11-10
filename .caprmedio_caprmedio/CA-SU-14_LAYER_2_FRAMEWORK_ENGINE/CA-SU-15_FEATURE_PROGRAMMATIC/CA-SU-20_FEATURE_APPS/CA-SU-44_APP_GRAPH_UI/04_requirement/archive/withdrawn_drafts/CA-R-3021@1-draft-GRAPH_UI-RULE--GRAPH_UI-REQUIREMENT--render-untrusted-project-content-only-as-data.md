---
identity:
  atom_id: CA-R-3021
  ref_id: CA-R-3021@1-draft
context:
  container:
    scope_unit: CA-SU-44
  role: Requirement
  form: Rule
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data
      Handling <+ Output Publication
    dependencies:
    - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
    - Project
  tier: 3
state:
  status: Draft
  version: 1
  updated_at: 2026-11-10 12:02:33 +0400
destination:
  file:
    name: CA-R-3021@1-draft-GRAPH_UI-RULE--GRAPH_UI-REQUIREMENT--render-untrusted-project-content-only-as-data.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-44_APP_GRAPH_UI/04_requirement/draft
author: Anatoly Maslennikov
relations:
  child_of:
  - CA-R-1076
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
---
## Summary
Render untrusted Project content only as data

## Claim

### Prose Claim

GRAPH_UI **must** render untrusted Project content as inspectable data **without** executing that content **or** granting it additional capabilities.

the boundary applies **in** **every** supported output context, including text, markup, links, styles, **and** control characters. displaying a value **must not** let that value escape its context **or** become executable authority. The choice of safe rendering technique remains Method-owned.
