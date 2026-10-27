---
atom_id: CA-P-2598
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
version: 6
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Workflow Orchestration/Action Realization
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2581
  depends_on:
  - CA-P-2597
  relates_to:
  - CA-R-1527
  - CA-R-1843
  - CA-R-1845
  - CA-M-328
  - CA-D-544
  - CA-O-016
tier: 3
---
# Summary

Validate Integrated Step result submissions

## Objective

Validate submitted result against the exact Project, Run, pending invocation, Workflow/Step/Action source binding, current candidate/test/input authority and admitted result labels. Preserve partial evidence and existing permissions; duplicate or mismatched submissions cannot execute effects again.

## Details

At most 15 minutes of own work per leaf; split before expanding. One Task per file. Review and update dependent Tasks after actual predecessor acceptance and before execution. Current source R1527@7 defines Integrated as the current participating session; a separate ephemeral CLI is not an Integrated implementation. Preserve existing native packet fields and current M/E/D guidance, explicit Project binding, source freshness, actual evidence and business-only Journal semantics. Use locked uv and configured Project Temporary State. Create a Concern for a real unresolved decision or blocker. No release, deployment, production MCP calls, full-suite run, uncertain replay or Git publication.

### Definition of Done

Retain exact changed paths/source bindings, focused functional and source-conformance evidence, observed limitations and the reviewed next dependent Task. Count fixture integrity, implementation, pending/current-session execution and runtime admission separately.

### Accepted completion evidence

The shared validator portfolio passed 28 focused checks and direct packet-binding checks passed 4. The isolated real-SDK MCP journey exercised the current 41-Method source frontier through three pending submissions (231 -> 232 -> 231), exact-duplicate acceptance, conflict refusal and terminal-blocked behavior. This closes the validation leaf only; the public status/privacy check, final public MCP review and separate runtime-admission gate remain outside this Task.
