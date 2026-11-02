---
subjects:
  governs: artifact-validation
  depends_on:
  - Subject/Engineering/Carrier
version: 15
updated_at: 2026-10-24 00:51:05 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-102@15
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Propagate Atom filename diagnostics

## Test case

**Fixture:** add one carrier that fails the malformed-filename fixture defined by CA-E-073 while leaving the rest of the project valid.

**Expected result:** fail with the propagated malformed-filename diagnostic **and** a non-zero exit.
