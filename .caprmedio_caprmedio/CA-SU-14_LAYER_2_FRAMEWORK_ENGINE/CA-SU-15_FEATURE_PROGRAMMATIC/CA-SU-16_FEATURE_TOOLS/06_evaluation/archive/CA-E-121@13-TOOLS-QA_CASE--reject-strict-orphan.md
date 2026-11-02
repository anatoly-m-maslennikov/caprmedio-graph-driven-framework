---
subjects:
  governs: artifact-validation
  depends_on:
  - Atom/Type
  - Authority Mode
version: 13
updated_at: 2026-10-23 03:17:34 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CAPRMEDIO-REQU-037
  - CA-R-1137
atom_id: CA-E-121@13
status: Archived
---
# Reject strict orphan

## Test case

**Fixture:** leave an Active non-Goal tier-classified RMED Atom parentless **in** a strict scope, with its applicable Type **not** registered as orphan-permitted under CAPRMEDIO-REQU-037. include a permitted orphan Type as a control.

**Expected result:** fail the non-exempt fixture with the stable strict-orphan diagnostic **and** a non-zero exit; do **not** reject the registered orphan-permitted control for parentlessness alone. this verdict diagnoses conformance **without** mutating the Atom, inventing a parent, **or** overriding the Operator's permission **to** retain a nonconforming Artifact.
