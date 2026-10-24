---
subjects:
  governs: artifact-validation
  depends_on: []
version: 12
updated_at: 2026-10-24 00:28:02 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-163@12
status: Archived
---
# Reject a skipped data stage

## Test case

**Fixture:** add one generated-data dependency that skips a required registered stage.

**Expected result:** fail with the stable data-stage-direction diagnostic **and** a non-zero exit.
