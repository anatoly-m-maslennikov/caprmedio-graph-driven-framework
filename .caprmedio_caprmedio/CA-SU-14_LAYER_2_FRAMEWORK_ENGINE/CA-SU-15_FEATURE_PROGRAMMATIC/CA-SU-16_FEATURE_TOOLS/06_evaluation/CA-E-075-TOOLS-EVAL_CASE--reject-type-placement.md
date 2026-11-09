---
atom_id: CA-E-075
ref_id: CA-E-075
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Validation"
tier: 2
relations:
  evaluation_for:
  - CA-R-1136
status: Active
version: 22
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject Type placement

## Test case

**Fixture:** place a valid Requirement-prefixed carrier **in** a Content-role directory that does **not** admit Requirement.

**Expected result:** fail with the stable Type-placement diagnostic **and** a non-zero exit.
