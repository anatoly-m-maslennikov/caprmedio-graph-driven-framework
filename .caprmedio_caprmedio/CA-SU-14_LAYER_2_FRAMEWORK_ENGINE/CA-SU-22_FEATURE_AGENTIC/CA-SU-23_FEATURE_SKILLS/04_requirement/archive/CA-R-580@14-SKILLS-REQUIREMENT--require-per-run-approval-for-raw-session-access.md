---
subject_scopes:
- session-access
version: 14
updated_at: 2026-10-24 01:33:47 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-1058
  - CA-R-1423
  - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: SKILLS
status: Archived
atom_id: CA-R-580@14
---
# Require per-run approval for raw session access

CAPRMEDIO **must** read raw session transcripts for a review run **only** **after** the operator explicitly approves that run **and** its bounded session scope.
