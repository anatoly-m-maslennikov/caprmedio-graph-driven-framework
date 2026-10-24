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
  - CA-R-1137
atom_id: CA-E-110@11
status: Archived
---
# Reject inverse backlink

## Test case

**Fixture:** store the inverse backlink for a relation already owned by its dependent Atom.

**Expected result:** fail with the stable inverse-backlink diagnostic **and** a non-zero exit.
