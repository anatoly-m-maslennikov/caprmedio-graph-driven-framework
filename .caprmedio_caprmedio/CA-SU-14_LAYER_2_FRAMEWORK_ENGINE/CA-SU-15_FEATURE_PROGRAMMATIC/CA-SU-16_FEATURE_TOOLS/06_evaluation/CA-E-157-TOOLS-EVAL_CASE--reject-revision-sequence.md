---
atom_id: CA-E-157
ref_id: CA-E-157
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Header.State.Version Number
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Header.State.Version Number
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Header.State.Updated At
  - Subject/CAPRMEDIO/Carrier
tier: 2
relations:
  evaluation_for:
  - CA-R-1415
  - CA-R-1492
  - CA-R-1137
status: Active
version: 23
updated_at: 2026-10-27 19:59:29 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject revision sequence

## Test case

**Fixture:** give an Atom a successive Revision whose Version does **not** increase under CA-R-1415. include a formatting-only Revision with an increased Version **and** the exact preceding Updated At value as a control under CA-R-1492.

**Expected result:** fail the non-increasing Version with the stable revision-sequence diagnostic **and** a non-zero exit. do **not** fail the formatting-only control because Updated At is unchanged. preserve other applicable Revision checks **without** treating a semantic change as formatting.
