---
topics:
  main_subject: Subject/CAPRMEDIO/Carrier/File.Extension
version: 21
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1136
atom_id: CA-E-098
ref_id: CA-E-098
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
form: Eval Case
tier: 2
container:
  scope_unit: CA-SU-16
---
# Reject carrier format

## Test case

**Fixture:** change the carrier extension **to** one **not** registered for its Artifact form.

**Expected result:** fail with the stable carrier-format diagnostic **and** a non-zero exit.
