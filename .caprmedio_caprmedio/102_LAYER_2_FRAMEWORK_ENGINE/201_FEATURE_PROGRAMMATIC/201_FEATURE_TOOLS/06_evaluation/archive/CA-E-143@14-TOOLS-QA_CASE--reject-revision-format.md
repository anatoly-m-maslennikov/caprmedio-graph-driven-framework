---
subjects:
  governs: artifact-validation
  depends_on: []
version: 14
updated_at: 2026-10-24 01:18:03 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-143@14
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
---
# Reject revision format

## Test case

**Fixture:** give one Atom an invalid version-and-timestamp revision format.

**Expected result:** fail with the stable revision-format diagnostic **and** a non-zero exit.
