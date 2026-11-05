---
atom_id: CA-E-116
ref_id: CA-E-116
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
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject downstream parent

## Test case

**Fixture:** point a tier-classified RMED child at a parent with a greater global tier number.

**Expected result:** fail with the stable downstream-parent diagnostic **and** a non-zero exit.
