---
atom_id: CA-P-2555
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2552]
  depends_on: [CA-P-2553]
version: 1
updated_at: "2026-10-21T16:54:03Z"
---
# Summary

Reconcile the technical-warning sink policy

## Objective

Apply the answered Logging Policy/configuration choice to the technical warning
boundary without turning warnings into business Journal records or hard-coding a
local/container sink.

## Details

At most 15 minutes own work after the Operator answers whether the configured
`.caprmedio_runtime/logs/` location is the default, container-only, or another
governed sink. Reuse CA-M-163, CA-D-396, CA-D-504 and CA-D-559; do not infer a
default from the current filesystem. Confirm warning records carry path/reason,
preserve `complete: false`, obey retention/back-pressure/unavailable-sink policy,
and leave historical/business Journal records unchanged. Root owns any runtime or
configuration implementation and deployment.

### Definition of Done

The explicit sink decision and focused logger evidence are recorded, or the Task
remains Backlog with the question and uncertainty preserved. No container-only
default, release acceptance, or deployment claim is allowed before then.
