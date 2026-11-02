---
subjects:
  governs: artifact-validation
  depends_on:
  - Atom/Type
  - Authority Mode
version: 13
updated_at: 2026-10-24 00:51:05 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CAPRMEDIO-REQU-030
  - CA-R-1137
atom_id: CA-E-122@13
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject a childless Principle in strict scope

## Test case

**Fixture:** leave an Active Principle **without** an active permitted child **in** a strict scope, with its applicable Type **not** registered as terminal under CAPRMEDIO-REQU-030. include a registered terminal Type as a control.

**Expected result:** fail the nonterminal fixture with the stable strict-child-coverage diagnostic **and** a non-zero exit. do **not** fail the registered terminal control for missing children alone; retain other applicable authority checks.
