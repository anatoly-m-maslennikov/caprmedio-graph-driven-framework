---
subjects:
  governs: artifact-validation
  depends_on: []
version: 11
updated_at: 2026-10-23 03:17:34 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1136
atom_id: CA-E-095@11
status: Archived
---
# Reject summary H1 mismatch

## Test case

**Fixture:** change the H1 so it no longer faithfully renders the immutable filename summary.

**Expected result:** fail with the stable summary-H1-mismatch diagnostic **and** a non-zero exit.
