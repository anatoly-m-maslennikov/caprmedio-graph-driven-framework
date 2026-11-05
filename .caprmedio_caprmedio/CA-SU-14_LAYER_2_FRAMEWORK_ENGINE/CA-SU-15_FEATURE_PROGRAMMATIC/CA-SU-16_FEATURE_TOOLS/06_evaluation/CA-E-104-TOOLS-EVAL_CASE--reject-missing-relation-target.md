---
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Relation.Target Reference
version: 20
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-104
ref_id: CA-E-104
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
form: Eval Case
tier: 2
container:
  scope_unit: CA-SU-16
---
# Reject missing relation target

## Test case

**Fixture:** point one relation at a nonexistent canonical filename stem.

**Expected result:** fail with the stable missing-relation-target diagnostic **and** a non-zero exit.
