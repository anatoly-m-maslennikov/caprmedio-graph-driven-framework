---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Summary
  depends_on: []
version: 18
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1136
atom_id: CA-E-095@18
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject summary H1 mismatch

## Test case

**Fixture:** change the H1 so it no longer faithfully renders the immutable filename summary.

**Expected result:** fail with the stable summary-H1-mismatch diagnostic **and** a non-zero exit.
