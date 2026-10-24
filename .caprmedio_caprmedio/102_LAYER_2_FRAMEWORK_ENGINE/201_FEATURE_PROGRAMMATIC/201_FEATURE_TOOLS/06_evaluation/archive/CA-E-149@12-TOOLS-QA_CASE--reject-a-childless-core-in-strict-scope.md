---
subjects:
  governs: artifact-validation
  depends_on:
  - Atom/Type
  - Authority Mode
version: 12
updated_at: 2026-10-24 00:28:02 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CAPRMEDIO-REQU-030
  - CA-R-1137
atom_id: CA-E-149@12
status: Archived
---
# Reject a childless Core in strict scope

## Test case

**Fixture:** leave an Active Core **without** an active permitted child **in** a strict scope, with its applicable Type **not** registered as terminal under CAPRMEDIO-REQU-030. include a registered terminal Type as a control.

**Expected result:** fail the nonterminal fixture with the stable strict-child-coverage diagnostic **and** a non-zero exit. do **not** fail the terminal control for missing children alone; retain other applicable authority checks.
