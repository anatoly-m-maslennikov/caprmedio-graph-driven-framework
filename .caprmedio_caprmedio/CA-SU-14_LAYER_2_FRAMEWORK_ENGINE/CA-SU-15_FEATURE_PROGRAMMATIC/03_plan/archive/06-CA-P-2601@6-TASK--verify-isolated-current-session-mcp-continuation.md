---
atom_id: CA-P-2601@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
version: 6
updated_at: '2026-10-22T19:51:48Z'
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2581
  depends_on:
  - CA-P-2600
  relates_to:
  - CA-R-1527
  - CA-R-1843
  - CA-R-1845
  - CA-M-328
  - CA-D-544
  - CA-O-016
---
# Summary

Verify isolated current-session MCP continuation

## Objective

Run the isolated current-session MCP journey from the current root APP entry and its observed binding. Prove prompt return, current-session result submission, next Step selection, stale/mismatched and repeated-submission safety, reconnect, two-Project isolation and unchanged Isolated behavior against the current 41-Method fixture. No live CLI or production endpoint.

## Details

At most 15 minutes of own work per leaf; split before expanding. One Task per file. Review and update dependent Tasks after actual predecessor acceptance and before execution. Current source R1527@7 defines Integrated as the current participating session; a separate ephemeral CLI is not an Integrated implementation. The route must be selected from the current root APP entry and its observed binding, not from a caller-supplied label or an inferred route. Bind the current 41-Method fixture and its exact source pins. Keep bounded response/receipt evidence in separate references (`CA-C-581` and `CA-P-2610`); those references are evidence inputs, not replacements for APP, RMED or Workflow authority. Preserve existing native packet fields and current M/E/D guidance, explicit Project binding, source freshness, actual evidence and business-only Journal semantics. Use locked uv and configured Project Temporary State. Create a Concern for a real unresolved decision or blocker. No release, deployment, production MCP calls, full-suite run, uncertain replay or Git publication.

### Definition of Done

Retain exact changed paths, source bindings and bounded response references for every journey. Record focused functional and source-conformance outcomes separately from fixture integrity, implementation behavior, pending/current-session execution and runtime admission. A passing isolated journey must not be reported as public MCP, production or deployed-runtime acceptance; leave the reviewed next dependent Task explicit.

### Accepted completion evidence

The real-SDK `test_interactive_mcp_journey.py` passed 4/4 in 31.770s, including the current 41-Method frontier, three pending submissions (231 -> 232 -> 231), public status/privacy, next-call token, exact duplicate, conflict refusal, terminal blocked status, source drift, oversize and tamper. This records the prior isolated current-session journey against the tested source-bound fixture; terminal public-status semantics remain unresolved under CA-C-582; the observed installed O016@13/CA-O-091 binding and separate runtime-admission gate remain with CA-P-2582 and the later handoff tasks.


The four SDK journey cases are distinct from the focused guards for two-Project isolation, unchanged Isolated behavior, restart durability and run-id retention; the latter are separate acceptance boundaries, not additional SDK journey cases.

### Reopened terminal-status checkpoint — 22 October 2026

The prior 4/4 journey result remains observed evidence, but the strengthened run exposed a real current-status defect: terminal submission retained the canonical terminal/interrupted_pending disposition and interrupted_pending graph result, while final public status returned blocked and required explicit recovery. Keep this Task Active for the bounded read-only verification in CA-P-2611. Do not replay completed Actions, mutate the Run through status inspection, or claim public/runtime admission.

### Accepted terminal-status repair — 22 October 2026

The strengthened current-workflow run and its read-only guards passed: terminal/interrupted_pending and interrupted_pending graph-result fields were retained from the same verified bytes, the final public status was correct, unknown root/child interruption did not fabricate a prompt, missing checkpoint stayed not_observed, and no recovery permission was granted. The focused portfolio passed 64/64, direct observation 6/6 and checkpoint 7/7; strict SDK 4/4 completed in 30.110s and final naked stdio exposed 23 tools. This closes the bounded status defect, not the broader binding/runtime/deployment gates.
