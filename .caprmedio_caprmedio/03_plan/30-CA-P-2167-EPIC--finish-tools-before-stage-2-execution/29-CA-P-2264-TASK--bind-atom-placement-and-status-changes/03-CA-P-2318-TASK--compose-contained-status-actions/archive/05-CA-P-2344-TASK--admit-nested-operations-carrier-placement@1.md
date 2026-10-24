---
atom_id: CA-P-2344
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
  governs: Tool
  depends_on: [Atom, Scope Unit, Workflow, Plan]
version: 1
updated_at: "2026-10-13 20:57:28 +0400"
relations:
  is_decomposition_of: [CA-P-2318]
---
# Summary

Admit nested Operations carrier placement

## Objective

Complete proposed-carrier validation admits source-defined nested Workflow/Step placements without admitting arbitrary folders.

## Details

Use current D467 and authenticated Workflow/Step same-stem parent carriers, role/status mapping and admitted source frontier. Replace the unconditional non-Plan depth refusal only for explicitly supported Operations containment. Prove ancestor identity/type/owner and legal Step child, preserve currentness and local status/history location. Do not infer containment from filename alone, weaken unrelated roles or skip complete validation. Wait until P2342's shared proposed_carrier.py changes freeze before mutation; root transfers ownership. Actual P2336 nested Step-to-Archived positive must pass afterward.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans/Git and serializes shared production files. Implementation and independent tests use disjoint scopes. No source-policy changes, live migration or invented relation semantics.

### Definition of Done

Current source/code/test pins, actual positive/refusal checks and independent acceptance establish the outcome. Required connected positives cannot be skipped or bypassed; preparation alone does not complete this Task.
