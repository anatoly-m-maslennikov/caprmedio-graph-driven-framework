---
atom_id: CA-R-580
ref_id: CA-R-580@20
container:
  scope_unit: CA-SU-23
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
tier: 1
relations:
  child_of:
  - CA-R-1058
  - CA-R-1423
  - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
status: Archived
version: 20
updated_at: 2026-10-27 20:00:10 +0400
subject_scopes:
- session-access
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: SKILLS
carrier_destination:
  file:
    name: CA-R-580@20-SKILLS-RULE--require-per-run-approval-for-raw-session-access.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-23_FEATURE_SKILLS/04_requirement/archive
---
## Summary

Require per-run approval for raw session access

## Claim

### Prose Claim

CAPRMEDIO **must** read raw session transcripts for a review run **only** **after** the operator explicitly approves that run **and** its bounded session scope.
