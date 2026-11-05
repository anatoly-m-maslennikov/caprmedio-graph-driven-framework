---
atom_id: CA-E-127
ref_id: CA-E-127
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  dependencies:
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Carrier
tier: 2
relations:
  evaluation_for:
  - CA-R-1483
  - CA-R-2688
  - CA-R-1137
  derived_from:
  - CA-A-057
status: Active
version: 24
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject unknown structural scope during project integrity validation

## Test case

**Fixture:** include CA-E-076's undeclared non-Project Scope Unit Carrier fixture **in** an otherwise conforming Project. resolve Scope Unit declarations from authoritative Project Structure, **not** arbitrary directory names; a Content Role folder, lifecycle folder, **or** Atom Collection **must not** become a Scope Unit merely because it is a folder.

**Expected result:** propagate the stable unknown-structural-scope diagnostic for the undeclared Scope Unit fixture with a non-zero exit. do **not** apply that diagnostic **to** an admitted non-Scope-Unit directory solely because it lacks a Scope Unit declaration.
