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
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Plan]
version: 1
updated_at: "2026-10-14 05:52:57 +0400"
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

