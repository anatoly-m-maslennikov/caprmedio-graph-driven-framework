---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on: []
version: 17
updated_at: 2026-10-24 11:58:20 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1136
atom_id: CA-E-083@17
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject unknown subject scope

## Test case

**Fixture:** add one subject token outside the vocabulary registered for the carrier's structural scope.

**Expected result:** fail with the stable unknown-subject-scope diagnostic **and** a non-zero exit.
