---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project
  depends_on: []
version: 18
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-101
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Accept a conforming project

## Test case

**Fixture:** validate a complete conforming project fixture containing registered Atoms, settings, current Projections, replayable Journals, **and** valid provenance.

**Expected result:** pass with exit `0`, an empty diagnostic set, **and** unchanged project bytes.
