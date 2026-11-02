---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Carrier
version: 19
updated_at: 2026-10-24 11:58:20 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1483
  - CA-R-1484
  - CA-R-1137
  derived_from:
  - CA-A-057
atom_id: CA-E-127@19
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject unknown structural scope during project integrity validation

## Test case

**Fixture:** include CA-E-076's undeclared non-Project Scope Unit Carrier fixture **in** an otherwise conforming Project. resolve Scope Unit declarations from authoritative Project Structure, **not** arbitrary directory names; a Content Role folder, lifecycle folder, **or** Atom Collection **must not** become a Scope Unit merely because it is a folder.

**Expected result:** propagate the stable unknown-structural-scope diagnostic for the undeclared Scope Unit fixture with a non-zero exit. do **not** apply that diagnostic **to** an admitted non-Scope-Unit directory solely because it lacks a Scope Unit declaration.
