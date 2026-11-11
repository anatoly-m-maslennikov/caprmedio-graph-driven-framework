---
atom_id: CA-R-2448
ref_id: CA-R-2448@7
container:
  scope_unit: CA-SU-00
role: Requirement
form: rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  - CAPRMEDIO_MODEL <+ Package/Implementation
tier: 2
relations:
  child_of:
  - CA-M-448
status: archived
version: 7
updated_at: "2026-11-11 14:54:13 +0400"
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
---
## Summary

Preserve valuable information

## Claim

### Prose Claim

Keep valuable Project information in durable, reliable storage so it remains recoverable across sessions, handoffs, context loss, and implementation changes.

## Semantics

A session or `MEMORY.md` may point to a durable copy, but neither counts as preservation on its own.
