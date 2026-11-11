---
atom_id: CA-P-2598@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
version: 2
updated_at: "2026-10-22T21:41:56+0400"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2581]
  depends_on: [CA-P-2597]
  relates_to: [CA-R-1527, CA-R-1843, CA-R-1845, CA-M-328, CA-D-544, CA-O-016]
---
# Summary

Validate Integrated Step result submissions

## Objective

Validate submitted result against the exact Project, Run, pending invocation, Workflow/Step/Action source binding, current candidate/test/input authority and admitted result labels. Preserve partial evidence and existing permissions; duplicate or mismatched submissions cannot execute effects again.

## Details

At most 15 minutes of own work per leaf; split before expanding. One Task per file. Review and update dependent Tasks after actual predecessor acceptance and before execution. Current source R1527@7 defines Integrated as the current participating session; a separate ephemeral CLI is not an Integrated implementation. Preserve existing native packet fields and current M/E/D guidance, explicit Project binding, source freshness, actual evidence and business-only Journal semantics. Use locked uv and configured Project Temporary State. Create a Concern for a real unresolved decision or blocker. No feature work before CA-P-2595 acceptance; no release, deployment, production MCP calls, full-suite run, uncertain replay or Git publication.

### Definition of Done

Retain exact changed paths/source bindings, focused functional and source-conformance evidence, observed limitations and the reviewed next dependent Task. Count fixture integrity, implementation, pending/current-session execution and runtime admission separately.
