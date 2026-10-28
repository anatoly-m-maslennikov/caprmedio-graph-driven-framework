---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Path
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Carrier
version: 21
updated_at: 2026-10-27 19:59:29 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-D-445
  - CA-R-1483
  - CA-R-1484
  - CA-R-1137
atom_id: CA-E-128
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject structural level address

## Test case

**Fixture:** give a Scope Unit using the default directory convention a directory address inconsistent with its declared level. include an explicit native binding admitted by CA-D-445 as a control, with different physical nesting **or** numeric tokens but unchanged declared parentage **and** Structural Level.

**Expected result:** fail the default-convention mismatch with the stable structural-level-address diagnostic **and** a non-zero exit. do **not** reject the admitted native control for its physical topology alone; retain its boundary, ownership, uniqueness **and** explicit-binding checks. do **not** derive a new structural declaration from either path.
