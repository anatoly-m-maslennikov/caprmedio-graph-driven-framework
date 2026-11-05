---
atom_id: CA-E-090
ref_id: CA-E-090
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Path
tier: 2
relations:
  evaluation_for:
  - CA-R-1136
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject stored scope path

## Test case

**Fixture:** persist `scope_path` **in** frontmatter **when** the canonical address derives it completely.

**Expected result:** fail with the stable derived-frontmatter-fact diagnostic **and** a non-zero exit.
