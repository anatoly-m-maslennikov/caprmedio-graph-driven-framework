---
atom_id: CA-E-128
ref_id: CA-E-128
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Path
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Scope Unit
  - Subject/CAPRMEDIO/Carrier
tier: 2
relations:
  evaluation_for:
  - CA-D-667
  - CA-R-1483
  - CA-R-2688
  - CA-R-1137
status: Active
version: 23
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject structural level address

## Test case

**Fixture:** give a Scope Unit using the default directory convention a directory address inconsistent with its declared level. include an explicit native binding admitted by CA-D-445 as a control, with different physical nesting **or** numeric tokens but unchanged declared parentage **and** Structural Level.

**Expected result:** fail the default-convention mismatch with the stable structural-level-address diagnostic **and** a non-zero exit. do **not** reject the admitted native control for its physical topology alone; retain its boundary, ownership, uniqueness **and** explicit-binding checks. do **not** derive a new structural declaration from either path.
