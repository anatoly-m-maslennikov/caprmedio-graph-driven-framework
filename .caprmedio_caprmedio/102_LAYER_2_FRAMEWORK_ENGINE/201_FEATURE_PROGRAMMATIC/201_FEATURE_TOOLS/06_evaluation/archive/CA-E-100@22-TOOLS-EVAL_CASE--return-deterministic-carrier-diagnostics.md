---
subjects:
  governs: Subject/Graph Node/Engineering/Verification/Static Analysis
  depends_on:
  - Subject/Graph Node/Carrier
version: 22
updated_at: 2026-10-27 06:04:45 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1136
atom_id: CA-E-100@22
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Return deterministic carrier diagnostics

## Test case

**Fixture:** run the malformed-filename fixture defined by CA-E-073 twice with the same settings **and** source frontier.

**Expected result:** return identical ordered diagnostics **and** exit status on both runs.
