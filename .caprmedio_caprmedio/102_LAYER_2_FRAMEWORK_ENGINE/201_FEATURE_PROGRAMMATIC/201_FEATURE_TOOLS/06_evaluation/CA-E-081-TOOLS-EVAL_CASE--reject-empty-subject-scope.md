---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Subjects
  depends_on: []
version: 19
updated_at: 2026-10-27 19:59:28 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1136
atom_id: CA-E-081
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject empty subject scope

## Test case

**Fixture:** make `subject_scopes` an empty list.

**Expected result:** fail with the stable empty-subject-scope diagnostic **and** a non-zero exit.
