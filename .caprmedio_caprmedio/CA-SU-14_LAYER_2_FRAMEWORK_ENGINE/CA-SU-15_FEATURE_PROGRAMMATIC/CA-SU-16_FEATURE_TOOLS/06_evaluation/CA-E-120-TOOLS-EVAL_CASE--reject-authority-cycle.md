---
atom_id: CA-E-120
ref_id: CA-E-120
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Relation/Type: child_of'
tier: 2
relations:
  evaluation_for:
  - CA-R-1137
  - CA-R-833
  - CA-E-481
  - CA-R-030
status: Active
version: 25
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject authority cycle

## Test case

**Fixture:** add one `child_of` edge that closes a cycle.

**Expected result:** fail with the stable authority-cycle diagnostic **and** a non-zero exit.
