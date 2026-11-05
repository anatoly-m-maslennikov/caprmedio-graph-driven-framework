---
atom_id: CA-E-119
ref_id: CA-E-119
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
# Reject backward authority

## Test case

**Fixture:** point a tier-classified RMED child at an Atom **in** a descendant structural scope.

**Expected result:** fail with the stable backward-authority diagnostic **and** a non-zero exit.
