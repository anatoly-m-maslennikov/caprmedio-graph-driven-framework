---
atom_id: CA-P-2542
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Node/Engineering/Occurrent/Runtime/Docker Workflow Execution
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2536
version: 5
updated_at: 2026-10-25 17:32:27 +0400
tier: 3
---
# Summary

Repair stale runtime image fallback test reference

## Objective

Restore the existing fallback-image regression to the current canonical constant owner without changing production behavior.

## Details

Root owns only tests/test_image_override.py under WORKFLOW_ORCHESTRATOR. Source edit waits for current full-suite terminal state; collect all failures first. Import or reference IMAGE from docker/image_reference.py, not removed runtime.IMAGE; do not add a compatibility export, alter fallback or loosen immutable validation. Existing runtime/image tests plus pinned Ruff/diff checks and independent review precede a NEW full Local release; focused success cannot replace full gate. At most15minutes own work. If additional failures arise, split them into separately recorded bounded owners before editing; preserve all unrelated work and exact planning predecessors.

### Focused source acceptance and next boundary

Canonical image_reference.IMAGE now supplies the expected fallback value; production image resolution and immutable validation are unchanged. Related image override/metadata14/14 pass0.280s; pinned Ruff/diff pass and independent review approves. Only two test lines changed. C568 resolves this test dependency failure, not full HEAD release acceptance.
