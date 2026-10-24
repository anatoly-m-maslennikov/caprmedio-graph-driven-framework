---
atom_id: CA-O-201@2
content_role: Operations
type: Workflow
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Workflow"
  depends_on: ["Atom","Scope Unit","Subject","Step","Workflow Run"]
version: 2
updated_at: "2026-10-12 23:49:24 +0400"
relations:
  relates_to: [CA-O-207, CA-O-046, CA-R-863, CA-M-372, CA-R-1509, CA-M-305]
---
# Summary

Find Atom targets

## Operation

Find Atom Targets **means** the independent read-only Workflow that returns the complete logical match set for one explicit discovery request through Step CA-O-207. It requires neither a subsequent Read nor Modify Workflow.

### Workflow graph

Entry: CA-O-207. On its confirmed complete-search result, terminate complete with the exact empty, singular or multiple match set. On invalid, stale, failed or incomplete discovery, terminate stopped with its attributable evidence. The graph has no second Step and invokes no effect or complete-Atom read.

### Request and result

The Workflow owns discovery criteria, explicit default selection if selected, and lifecycle/frontier inclusion before supplying O046's D625 `query` request. The request explicitly declares the Scope Unit frontier, lifecycle inclusion and logical predicates, including Subjects `governs`/`depends_on` and exact, prefix, suffix or contains matching under the selected profile. An Active default must not omit other eligible non-archived statuses when a caller requests the full non-archived frontier. Preserve invalid-source diagnostics and completeness evidence; do not infer membership.

Return Atom IDs, Versions, owning Scope Units and the requested matched values. A Find-reference receiving use selects explicit reference criteria and returns owning Atom targets; it does not retarget references or automatically invoke O202. Full reading remains the separately callable O047 Action; storage details remain private.

## Details

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
