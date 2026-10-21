---
atom_id: CA-P-2542
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2536]
version: 1
updated_at: "2026-10-21T12:40:32Z"
---
# Summary

Repair stale runtime image fallback test reference

## Objective

Restore the existing fallback-image regression to the current canonical constant owner without changing production behavior.

## Details

Root owns only tests/test_image_override.py under WORKFLOW_ORCHESTRATOR. Source edit waits for current full-suite terminal state; collect all failures first. Import or reference IMAGE from docker/image_reference.py, not removed runtime.IMAGE; do not add a compatibility export, alter fallback or loosen immutable validation. Existing runtime/image tests plus pinned Ruff/diff checks and independent review precede a NEW full Local release; focused success cannot replace full gate. At most15minutes own work. If additional failures arise, split them into separately recorded bounded owners before editing; preserve all unrelated work and exact planning predecessors.
