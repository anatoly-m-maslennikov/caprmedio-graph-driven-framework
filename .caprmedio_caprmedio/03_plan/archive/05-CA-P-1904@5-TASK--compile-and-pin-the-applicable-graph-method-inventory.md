---
atom_id: CA-P-1904@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - Subject/Engineering/Evaluation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Subject/Engineering/Operations
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 10:29:57 +0400
relations:
  is_decomposition_of:
  - CA-P-1898
tier: 3
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
