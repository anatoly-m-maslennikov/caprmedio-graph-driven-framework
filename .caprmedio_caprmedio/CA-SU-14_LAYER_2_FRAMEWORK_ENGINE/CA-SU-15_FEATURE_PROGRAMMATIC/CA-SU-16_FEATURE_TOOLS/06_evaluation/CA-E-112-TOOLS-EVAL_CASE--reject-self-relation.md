---
atom_id: CA-E-112
ref_id: CA-E-112
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Relation/Type: child_of'
  dependencies:
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject
tier: 2
relations:
  evaluation_for:
  - CA-R-833
  - CA-R-879
  - CA-E-481
  - CA-R-1137
status: Active
version: 22
updated_at: 2026-10-27 19:59:28 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject self relation

## Test case

**Fixture:** point an active normative-authority `child_of` Relation from an Atom **to** itself under CA-R-879. this self-edge creates a cycle prohibited by CA-R-833; do **not** infer a universal self-edge prohibition for other graph kinds **or** Relation Kinds.

**Expected result:** fail with the stable self-relation diagnostic **and** a non-zero exit.
