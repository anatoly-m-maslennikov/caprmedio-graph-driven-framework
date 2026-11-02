---
atom_id: CA-O-207@2
content_role: Operations
type: Step
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Step"
  depends_on: ["Search Atom Carriers","Step Run","Workflow Run"]
version: 2
updated_at: "2026-10-12 23:49:24 +0400"
relations:
  relates_to: [CA-O-201, CA-O-046, CA-R-1509, CA-R-1511, CA-M-305]
---
# Summary

Find targets through Atom Search

## Operation

This Step invokes exactly CA-O-046 for one O201 discovery request. It is read-only and supplies no effect permission.

### Input and parameter binding

Bind Scope Unit frontier, logical predicates, explicit lifecycle inclusion, requested match values and selected Subject profile/grammar evidence from O201's checked explicit request. O201 owns criteria/default decisions; supply O046 operation `query` and the common D625 query, expected_state and authorization/context bindings. Bind every required O046 input from that request and current declared authority, plus exact Action/Step/Workflow definition pins and actual Run context before dispatch; reject an absent, stale or ambiguous binding. Private traversal/source evidence comes from the selected independently verified realization, never a public path selector.

Return O046's exact complete match set or failed/incomplete outcome without inventing members or full-Atom reads. O201 alone maps that result to its terminals. No other Action or Workflow is invoked here.

## Details

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
