---
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Data Handling/Data Validation
  depends_on: []
version: 19
updated_at: 2026-10-26 00:46:35 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1136
atom_id: CA-E-073@19
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject malformed filename

## Test case

**Fixture:** remove one required segment from the canonical filename grammar.

**Expected result:** fail with the stable malformed-filename diagnostic **and** a non-zero exit.
