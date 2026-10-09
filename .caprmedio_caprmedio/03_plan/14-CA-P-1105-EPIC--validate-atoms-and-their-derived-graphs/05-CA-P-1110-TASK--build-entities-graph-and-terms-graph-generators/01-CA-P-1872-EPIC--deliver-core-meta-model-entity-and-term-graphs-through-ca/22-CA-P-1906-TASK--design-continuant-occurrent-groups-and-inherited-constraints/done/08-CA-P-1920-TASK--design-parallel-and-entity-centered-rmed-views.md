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
status: Done
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 2
updated_at: "2026-10-10 02:32:12 +0400"
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

### Local execution receipt

Own work completed on 2026-10-10 02:32:12 +0400. Independent read-only acceptance passed: 908 current source pins, all 4534 baseline occurrence accounting, shared catalog and both compact trees reproduce exactly. These are pointer-derived associations, not proven semantic applicability.

- `.caprmedio_caprmedio/_projection/core-entity-review/design/rmed.views.json`, SHA-256 `d7fd113a408c3bb70e17ab55cc86fd6746c3d5c74ff27a9a864632ec6de999aa`.
- `.caprmedio_caprmedio/_projection/core-entity-review/design/rmed.views.md`, SHA-256 `7365beeec9e62620fab5ee78855497fb37180f77c7235a14c545b5c3f24afc7f`.
- `.caprmedio_caprmedio/_projection/core-entity-review/design/rmed.roles.indented.txt`, SHA-256 `191b54635829256aebb9b4fcb8489cddfd1c80ee22e406de43cfea68fd2844d7`.
- `.caprmedio_caprmedio/_projection/core-entity-review/design/rmed.entities.indented.txt`, SHA-256 `17a4d3661cb73702dded836cc3fad968e63faf57e29ba0eed8ffd8fe8eec9172`.

Baseline inventory fingerprint: `23394abaf6e9c18a585cf3146aedd0a80df166c9dd82be6e86ed7c3c56780bdc`. Current source pins, exact positive evidence spans and complete assigned case/pointer coverage passed. No Core, Subject, history, Step 1, runtime, Run or Journal change is claimed. This receipt completes only the bounded review output, not the parent design, candidate acceptance or migration.

### Definition of Done

the Plan is **not** Done **if** ((a shared source Claim is duplicated as authority **or** optional M/E/D is made mandatory **or** pointer incidence is asserted as a new native relation **or** either requested view is missing) **or** (a required start prerequisite is **not** Done) **or** (the stated output or handoff is missing) **or** (uncertainty below 90% is silently decided or its question is not put to the Operator) **or** (source pins or checks are stale) **or** (the exclusive boundary is exceeded) **or** (any direct decomposing Plan is **not** Done)).
