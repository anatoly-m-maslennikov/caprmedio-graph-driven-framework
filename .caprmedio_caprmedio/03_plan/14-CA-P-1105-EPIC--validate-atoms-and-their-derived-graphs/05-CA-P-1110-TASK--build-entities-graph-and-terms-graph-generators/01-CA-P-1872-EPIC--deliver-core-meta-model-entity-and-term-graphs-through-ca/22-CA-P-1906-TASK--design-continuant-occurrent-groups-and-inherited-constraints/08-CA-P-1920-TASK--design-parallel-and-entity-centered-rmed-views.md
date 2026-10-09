---
atom_id: CA-P-1920
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 1
updated_at: "2026-10-10 02:10:14 +0400"
relations:
  is_decomposition_of: [CA-P-1906]
  blocks: [CA-P-1921]
---
# Summary

Design parallel and Entity centered RMED views

## Objective

Design both derived RMED presentations from shared source identities, without creating duplicate authority or mandatory M/E/D slots.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Required start prerequisite: CA-P-1905. Inputs: the completed pinned baseline and the explicit partition or design contract.

Deliver separate R/M/E/D overview trees and an Entity-centered view with applicable M/E/D links. R presents the Entity-model skeleton and required results; M construction/Implementation conventions; E checks and acceptance criteria; D Carrier models, formats, storage and placement. A shared Claim may apply to several Entities; link it once, and omit empty M/E/D slots unless required by authority.

The existing `/`, `.` and `:` operators describe Entity-model relations, not M/E/D attachments. Keep exact governs and depends_on pointers distinct; a dependency is not a governing Claim or automatic applicability. Keep Carrier definitions from Delivery sources. Internal/External/Relational is orthogonal, not a partition of Entity identities. Output `rmed.views.json` and `rmed.views.md` in `.caprmedio_tmp/planning/core-entity-review/design/`, with exact source references, pointer-based view memberships, concrete examples and any applicability limits.

Read current Core Main Content and verify exact source pins before proposing meaning. Earlier classification caches are preparation only. Below 90% confidence, leave a proposal unresolved, state the missing evidence and put the question to the Operator before deciding. A diagnostic or proposed view is not native admission. Preserve all qualified identities and do not infer Entity facts from source Atom metadata or Subject incidence. Work locally without MCP or FPF; do not change Core Atoms, Subjects, history, baseline outputs, implementation, runtime or unrelated work.

### Definition of Done

the Plan is **not** Done **if** ((a shared source Claim is duplicated as authority **or** optional M/E/D is made mandatory **or** pointer incidence is asserted as a new native relation **or** either requested view is missing) **or** (a required start prerequisite is **not** Done) **or** (the stated output or handoff is missing) **or** (uncertainty below 90% is silently decided or its question is not put to the Operator) **or** (source pins or checks are stale) **or** (the exclusive boundary is exceeded) **or** (any direct decomposing Plan is **not** Done)).
