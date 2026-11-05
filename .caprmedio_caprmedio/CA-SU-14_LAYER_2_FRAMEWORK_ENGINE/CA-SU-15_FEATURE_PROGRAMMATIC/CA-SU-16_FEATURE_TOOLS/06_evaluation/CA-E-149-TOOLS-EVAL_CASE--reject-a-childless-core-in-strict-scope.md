---
atom_id: CA-E-149
ref_id: CA-E-149
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Rule
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Type
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings.Authority Modes
tier: 2
relations:
  evaluation_for:
  - CA-R-030
  - CA-R-1137
status: Active
version: 22
updated_at: 2026-10-27 19:59:29 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject a childless Core in strict scope

## Test case

**Fixture:** leave an Active Core **without** an active permitted child **in** a strict scope, with its applicable Type **not** registered as terminal under CA-R-030. include a registered terminal Type as a control.

**Expected result:** fail the nonterminal fixture with the stable strict-child-coverage diagnostic **and** a non-zero exit. do **not** fail the terminal control for missing children alone; retain other applicable authority checks.
