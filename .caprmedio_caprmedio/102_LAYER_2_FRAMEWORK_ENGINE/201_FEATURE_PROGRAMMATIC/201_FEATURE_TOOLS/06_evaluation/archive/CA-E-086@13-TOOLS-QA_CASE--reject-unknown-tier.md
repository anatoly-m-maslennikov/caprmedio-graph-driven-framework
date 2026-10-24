---
subjects:
  governs: artifact-validation
  depends_on:
  - Atom/Tier/Local Tier
  - Subject/Engineering/Carrier
version: 13
updated_at: 2026-10-23 03:18:40 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-D-285
  - CA-R-1136
atom_id: CA-E-086@13
status: Archived
---
# Reject unknown tier

## Test case

**Fixture:** give an ordinary RMED Atom an unregistered Local Tier token at the registered Local Tier position **in** its otherwise valid filename under CA-D-285; do **not** encode the tier **in** frontmatter.

**Expected result:** fail with the stable unknown-tier diagnostic **and** a non-zero exit.
