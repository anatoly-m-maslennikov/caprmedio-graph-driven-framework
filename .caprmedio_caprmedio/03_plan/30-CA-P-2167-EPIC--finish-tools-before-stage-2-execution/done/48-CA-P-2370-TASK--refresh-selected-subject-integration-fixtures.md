---
atom_id: CA-P-2370
content_role: Plan
type: Plan
label: Task
work_sequence_number: 48
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Plan]
version: 2
updated_at: "2026-10-14 06:05:07 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Refresh selected Subject integration fixtures

## Objective

Repair only stale selected Subject apply/recovery fixtures after comparing historical and current governing definitions. Preserve old historical fixtures; use a current fixture where necessary. Never rewrite production binding manifests, relax validators or substitute new hashes without checking meaning. Keep current subject contract changes serialized with the owner.

## Details

Estimated own work: up to 15 minutes; split before exceeding this bound. Root owns integration, Plans and Git. Workers use disjoint assigned files and preserve unrelated edits. This is necessary Subjects-only migration tooling; Core migration, ordinary content edits, legacy C/A repair, catalogs and unrelated connector work remain outside this Task.

### Definition of Done

Relevant isolated selected Subject apply, effect-portfolio and recording-recovery tests run against the intentionally current source packet with preserved safety assertions. Record exact sources and remaining independent manifest failures. Test fixture success is not production MCP or live migration acceptance.

### Accepted bounded outcome

Refreshed only test_subject_apply_portfolio.py. Exact archived and current O127/O128/O129 hashes were verified before adopting v4/v6/v4: their changes clarify separately admitted containment cascades and preserve this single-target Update route. The fixture now declares its actual Project identity and CA prefix inside its temporary root; production validation remains unchanged.

All 39 focused selected Subject apply, independent effect-portfolio and recording-recovery tests passed in 215.4 seconds. Independent fixture review passed; final file SHA-256 `9d9b827227f356047771c9c52e7de5fe5c53df2e00dbc9c780f6f6612c35b6bd`. No extra D531 pin repair was needed. The production selected-route manifest still references old paths and was not edited; installed MCP and live Subject migration remain open.

