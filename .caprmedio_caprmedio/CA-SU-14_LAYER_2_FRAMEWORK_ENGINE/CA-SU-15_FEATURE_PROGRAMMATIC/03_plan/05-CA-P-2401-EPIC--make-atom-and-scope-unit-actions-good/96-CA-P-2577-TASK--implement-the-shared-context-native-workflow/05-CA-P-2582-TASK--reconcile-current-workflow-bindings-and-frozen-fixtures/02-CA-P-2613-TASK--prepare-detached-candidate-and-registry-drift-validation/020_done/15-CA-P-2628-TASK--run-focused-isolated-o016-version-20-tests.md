---
atom_id: CA-P-2628
ref_id: CA-P-2628
container:
  atom: CA-P-2613
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Implementation Evaluation
tier: 3
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
status: Done
version: 6
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 15-CA-P-2628-TASK--run-focused-isolated-o016-version-20-tests.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/05-CA-P-2582-TASK--reconcile-current-workflow-bindings-and-frozen-fixtures/02-CA-P-2613-TASK--prepare-detached-candidate-and-registry-drift-validation/020_done
work_sequence_number: 15
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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
