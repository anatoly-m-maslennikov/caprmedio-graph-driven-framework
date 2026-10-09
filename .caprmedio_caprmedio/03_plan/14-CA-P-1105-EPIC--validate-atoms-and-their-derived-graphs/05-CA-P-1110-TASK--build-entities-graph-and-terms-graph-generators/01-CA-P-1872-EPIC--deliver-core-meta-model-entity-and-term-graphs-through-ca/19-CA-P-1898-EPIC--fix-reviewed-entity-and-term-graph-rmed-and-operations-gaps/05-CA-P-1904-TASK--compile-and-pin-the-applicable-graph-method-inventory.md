---
atom_id: CA-P-1904
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Projection
  depends_on: [Requirement, Method, Evaluation, Delivery, Operations, Plan]
version: 1
updated_at: "2026-10-09 19:23:34 +0400"
relations:
  is_decomposition_of: [CA-P-1898]
---
# Summary

Compile and pin the applicable graph Method inventory

## Objective

Compile and pin the applicable graph Method inventory.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Inputs: Current Project Structure, repaired graph packet and authoritative Method carrier universe.

Required Plan prerequisites: CA-P-1903.

Output and acceptance: Retain full-content current Method inventory, exact path/revision/hash, explicit status/role limitations and currentness recheck for independent acceptance.

Exclusive scope: Derived scratch inventory under .caprmedio_tmp/planning/core-meta-model-graphs only; authoritative Methods read-only.

Inherit the main Epic's local-without-MCP authorization and 90% question threshold. Preserve identities and Summaries, advance changed carrier revisions, and bind actual source evidence. Split before further work if this leaf exceeds its bounded responsibility. These repairs and their review records are not live Run or Journal receipts.

### Definition of Done

the Plan is **not** Done **if** ((the stated source-backed output **or** required verification is missing) **or** (a required check is failed, unresolved, stale **or** unverified) **or** (work exceeds the admitted boundary) **or** (any direct decomposing Plan is **not** Done)).
