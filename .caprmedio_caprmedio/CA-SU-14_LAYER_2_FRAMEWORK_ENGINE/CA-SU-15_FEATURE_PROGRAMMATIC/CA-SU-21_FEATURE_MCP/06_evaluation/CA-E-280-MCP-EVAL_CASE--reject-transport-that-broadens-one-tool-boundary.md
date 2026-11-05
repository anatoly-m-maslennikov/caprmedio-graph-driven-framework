---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
version: 17
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-M-174
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-280
ref_id: CA-E-280
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
form: Eval Case
tier: 3
container:
  scope_unit: CA-SU-21
---
# Reject transport that broadens one Tool boundary

## Claim checked

MCP cannot alter a canonical Tool's authority, cardinality, failure, **or** side-effect boundary.

## Test case

Forward one Atom Doer request while attempting **to** substitute a broader target set **or** success for a partial Tool outcome.

## Acceptance criteria

the request is rejected **or** the exact Tool outcome is retained; no broader **or** fabricated success crosses the boundary.

## Failure disposition

Stop the invocation **and** record the attempted semantic alteration.
