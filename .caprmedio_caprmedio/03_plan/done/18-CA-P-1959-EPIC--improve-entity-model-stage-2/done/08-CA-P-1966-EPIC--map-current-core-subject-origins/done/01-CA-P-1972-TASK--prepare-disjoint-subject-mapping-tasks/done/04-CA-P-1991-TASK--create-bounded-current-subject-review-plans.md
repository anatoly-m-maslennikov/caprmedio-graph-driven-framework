---
atom_id: CA-P-1991
ref_id: CA-P-1991
role: Plan
form: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
topics:
  main_subject: Subject
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject
  - Subject/Graph Node/Domain/Continuant/Projection
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
version: 7
updated_at: 2026-11-02 19:44:26 +0400
relations:
  is_decomposition_of:
  - CA-P-1972
tier: 3
container:
  atom: CA-P-1972
carrier_destination:
  file:
    name: 4-CA-P-1991-TASK--create-bounded-current-subject-review-plans.md
    path: .caprmedio_caprmedio/03_plan/done/18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/8-CA-P-1966-EPIC--map-current-core-subject-origins/done/1-CA-P-1972-TASK--prepare-disjoint-subject-mapping-tasks/done
---
# Summary

Create bounded current Subject review Plans

## Objective

Give every verified batch one bounded review owner and define complete ledger integration.

## Details

Estimated own work: 15 minutes. Inherit CA-P-1959 and CA-P-1972 boundaries. This decomposition records the expanded preparation work; it does not pretend the rejected first inventory was accepted.

Prerequisites: CA-P-1988, CA-P-1989 and CA-P-1990 Done. Generate review Tasks directly under CA-P-1966 from exact verified batch pins; assign each source/occurrence to one Task. Each Task is estimated at most 15 minutes, with decomposition if needed. Add one ledger integration Task with all reviews as prerequisites and actual coverage/evidence checks. Keep new Source mappings, grammar and Core writes out of this preparation. Output: support/prepare_subject_mapping_plans.py, created review/integration Plans, ownership manifest and verification receipt.

Root owns shared integration and Git. Preserve other workers' edits. Use uv and .caprmedio_tmp for scratch. No MCP/FPF, authority, runtime or captured-review mutation. Creating this Plan does not complete its checks.

### Definition of Done

Not Done if the required evidence/output is missing or stale, coverage or independent checks fail, a Source or captured artifact changes, unsupported authority/adoption is claimed, or own work exceeds 15 minutes without decomposition.
