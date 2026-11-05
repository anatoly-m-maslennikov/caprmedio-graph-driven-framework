---
atom_id: CA-P-2501
ref_id: CA-P-2501
container:
  atom: CA-P-2494
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Domain/Continuant/Atom
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2494
status: Active
version: 4
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 5-CA-P-2501-TASK--wire-container-lifecycle-entrypoints.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/66-CA-P-2494-TASK--compose-recursive-container-lifecycle-actions
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Wire container lifecycle entrypoints

## Objective

Connect the sealed container preview and technical coordinator to actual MCP/worker/status entrypoints.

## Details

At most 15 minutes own work; split before extending. Root owns existing selected_routes.py, selected_native_providers.py and backend.py plus focused integration tests. Depend on P2500 pure seal and P2499 caller interface. Preserve one-Atom lifecycle_admission unchanged; add separate observed.container_lifecycle only to root MCP preview. Worker verifies original full seal then ordinary per-member admissions. Status must identify technical coordinator separately from actual member Runs and never invent a terminal root Workflow Run. No production MCP port, dependency, release, deployment or migration.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
