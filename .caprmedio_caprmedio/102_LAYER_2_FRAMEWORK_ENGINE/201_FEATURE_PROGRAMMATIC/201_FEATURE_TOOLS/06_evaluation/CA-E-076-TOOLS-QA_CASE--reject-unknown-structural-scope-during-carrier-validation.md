---
subjects:
  governs: artifact-validation
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Carrier
version: 18
updated_at: 2026-10-24 02:14:24 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1483
  - CA-R-1484
  - CA-R-1136
  derived_from:
  - CA-A-057
atom_id: CA-E-076
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject unknown structural scope during carrier validation

## Test case

**Fixture:** place the Carrier under a non-Project Scope Unit absent from the owning Project's accepted Project Structure declarations. keep Project Settings valid for the Project root identity; a folder observation **or** Goal **must not** substitute for a missing declaration under CA-R-1483 **and** CA-R-1484.

**Expected result:** fail with the stable unknown-structural-scope diagnostic **and** a non-zero exit.
