---
atom_id: CA-P-2628@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 15
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 5
updated_at: 2026-10-24 10:35:14 +0400
subjects:
  governs: Subject/Engineering/Implementation Evaluation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2613
  depends_on:
  - CA-P-2627
  - CA-P-2612
  relates_to:
  - CA-O-016
  - CA-C-584
  - CA-R-1847
  - CA-E-567
tier: 3
---
# Summary

Run focused isolated O016 version 20 tests

## Objective

Run the bounded isolated functional checks for current O016@20 compatibility after verified body equivalence and the CA-P-2627 proposal. Keep the public default route at the exact 15-operation contract; test optional move_atom only as an explicit implementation capability, not as current public admission.

## Details

Owner lane: journal_compiler_repair. This is one Task with at most 15 minutes of own work. Use the frozen or explicitly admitted current-source fixture and a non-live test harness. Cover current O016@20, the unchanged legacy-17/direct-18 compatibility boundary, explicit optional support, response shape and failure visibility. Do not broaden to every version greater than 18, mutate source or Project bindings, run production MCP, replay calls, release, deploy or rerun the full suite.

## Definition of Done

Return focused isolated test results and any residual compatibility blocker, tied to the verified O016@20 body and exact input/source pins. Passing checks do not publish or admit a live binding and do not resolve CA-C-584 by themselves.

## Completion evidence — 23 October 2026

The O016@20 code-admission and focused isolated checks passed: the reported
portfolio contains 34 focused checks, with Ruff and strict Mypy also passing.
Independent Terra review found no findings, including for the exact allowlist,
boolean/unknown refusal, canonical mapping, no MCP queue fallback, and
operative dispatch. Two separate Root registration checks passed in 6.649
seconds. These are focused code/test results, not live binding admission; no
Project binding changed, route was published, production MCP was run, release
or deployment occurred, or full suite was rerun. CA-C-584 remains a separate
frontier reconciliation concern.
