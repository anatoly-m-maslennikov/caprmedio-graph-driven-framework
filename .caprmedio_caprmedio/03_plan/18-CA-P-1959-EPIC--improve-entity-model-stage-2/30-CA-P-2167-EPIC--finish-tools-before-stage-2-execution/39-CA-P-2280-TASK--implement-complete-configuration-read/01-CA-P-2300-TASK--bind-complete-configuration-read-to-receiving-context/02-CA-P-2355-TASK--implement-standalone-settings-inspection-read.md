---
atom_id: CA-P-2355
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Configuration, Workflow, Journal, Plan]
version: 1
updated_at: "2026-10-13 22:24:17 +0400"
relations:
  is_decomposition_of: [CA-P-2300]
---
# Summary

Implement standalone Settings inspection Read

## Objective

Implement a standalone no-legacy Project Settings inspection reader using CA-P-2354's accepted complete schema/source bindings. Return the accepted typed immutable Settings snapshot and exact provenance with no effects.

## Details

Own only the new standalone inspection path and its focused tests. Preserve exact observed source evidence in the typed immutable snapshot and provenance. Accept schema-valid supplied Settings with unknown history without migrating existing Settings or callers. Unknown logical Revision or currentness must remain explicit; a digest or successful parse does not establish them. Preserve the history distinction and require separate admission for any operation that needs verified history. Do not add a generic native TOML text/document API, a new receiving or Session route, legacy recovery, history inference, publication, Journal writes or runtime changes.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git. Parallel workers own disjoint files; preserve unrelated changes. This Task does not authorize changes to existing Settings documents, existing callers, Journal or runtime.

### Definition of Done

Focused checks prove the accepted complete typed immutable Settings snapshot and exact source provenance, schema/source refusals, stale-state refusal and zero effects. A schema-valid unknown-history document reads successfully; malformed/partial data refuse, and inspection success cannot grant verified-history operation permission. Exact implementation/test evidence and independent review establish this bounded path. Complete Configuration Read receiving integration, parent-wide and runtime completion remain separate.
