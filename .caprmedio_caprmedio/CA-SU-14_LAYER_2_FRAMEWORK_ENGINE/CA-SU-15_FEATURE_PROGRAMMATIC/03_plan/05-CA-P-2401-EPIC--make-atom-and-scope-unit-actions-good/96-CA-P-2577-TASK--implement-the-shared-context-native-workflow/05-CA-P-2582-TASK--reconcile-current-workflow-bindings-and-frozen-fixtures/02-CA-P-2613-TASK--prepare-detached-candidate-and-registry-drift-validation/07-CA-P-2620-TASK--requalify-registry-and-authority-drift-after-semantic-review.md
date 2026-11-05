---
atom_id: CA-P-2620
ref_id: CA-P-2620
container:
  atom: CA-P-2613
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/MCP.selected Workflow route contract
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2613
  depends_on:
  - CA-C-583
  - CA-C-584
  - CA-P-2612
  relates_to:
  - CA-A-1142
  - CA-W-09
  - CA-C-576
status: Backlog
version: 6
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 7-CA-P-2620-TASK--requalify-registry-and-authority-drift-after-semantic-review.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/5-CA-P-2582-TASK--reconcile-current-workflow-bindings-and-frozen-fixtures/2-CA-P-2613-TASK--prepare-the-detached-candidate-and-registry-drift-validation/001_backlog
work_sequence_number: 7
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Requalify registry and authority drift after semantic review

## Objective

After CA-C-583 and CA-C-584 are resolved or explicitly accepted, requalify the
detached source inventory, A1142/W09 registry distinction and current 15 versus
optional 16-operation contract. Keep the visible Project binding and all
authority carriers unchanged.

## Details

This is one bounded review Task with at most 15 minutes of own work. Reuse the
accepted five source pins, the 50-pin revalidation and unchanged Project,
Engine, A1142, R1525, R1720 and D340 baselines. Report exact current-source
membership, contract scope and unresolved drift. Do not fix source, emit or
admit a candidate, mutate a manifest or projection, run production MCP,
implement Scope Units, replay calls, release or deploy.

## Definition of Done

Produce one compact registry/authority report with explicit Problem decisions,
source IDs, versions, paths and hashes. The report must distinguish semantic
acceptance from mechanical equality and leave candidate compilation as a
separate dependent Task.

### C584 candidate-direction checkpoint — 23 October 2026

The source-contract question now has a candidate-resolution direction: a
detached candidate must omit optional move_atom, while preserving the
optional implementation capability for a later compatible frontier decision.
O127's internal Move capability does not admit a public MCP route. The live
Project manifest remains at 16 operations and is untouched until a separately
validated publication decision. Keep CA-C-584 Active until that correction is
validated; this Task may requalify the candidate afterward, but it does not
claim runtime, public-contract, manifest or publication completion.
