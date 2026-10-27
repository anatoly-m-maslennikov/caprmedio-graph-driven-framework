---
atom_id: CA-P-2600
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
version: 6
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/MCP.selected Workflow capability routes
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2581
  depends_on:
  - CA-P-2599
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

Expose Integrated continuation through Project MCP

## Objective

Add the narrow public submission/continuation surface using existing Project/request/Run/source fields and selected-route ownership. Preserve legacy preview/execute/status behavior and explicitly Isolated callbacks. Keep pending prompt frontiers observable without declaring Workflow completion.

## Details

At most 15 minutes of own work per leaf; split before expanding. One Task per file. Review and update dependent Tasks after actual predecessor acceptance and before execution. Current source R1527@7 defines Integrated as the current participating session; a separate ephemeral CLI is not an Integrated implementation. Preserve existing native packet fields and current M/E/D guidance, explicit Project binding, source freshness, actual evidence and business-only Journal semantics. Use locked uv and configured Project Temporary State. Create a Concern for a real unresolved decision or blocker. No feature work before CA-P-2595 acceptance; no release, deployment, production MCP calls, full-suite run, uncertain replay or Git publication.

### Definition of Done

Retain exact changed paths/source bindings, focused functional and source-conformance evidence, observed limitations and the reviewed next dependent Task. Count fixture integrity, implementation, pending/current-session execution and runtime admission separately.

### Accepted completion evidence

The real-SDK `test_interactive_mcp_journey.py` passed 4/4 in 31.770s, covering three pending submissions (231 -> 232 -> 231), public status/privacy, the next-call token, exact duplicates, conflict refusal, terminal-blocked and blocked-status behavior, source drift, oversize and tamper. Root entry checks passed 4 and the legacy orchestrator portfolio passed 30 in 157s; the naked stdio smoke passed with 23 valid tools and an exact-path preview. The current installed binding remains a separate CA-P-2582 reconciliation gate (the observed artifact is still O016@13/CA-O-091); this Task closes the focused public-surface implementation evidence only, not current Project binding or runtime admission.

