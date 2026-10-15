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
  depends_on: [Atom, Configuration, Plan]
version: 2
updated_at: "2026-10-13 22:57:09 +0400"
relations:
  is_decomposition_of: [CA-P-2300]
---
# Summary

Implement ordinary Settings file reader

## Objective

Implement a standalone no-legacy reader that reads the supplied Settings file, parses it and validates CA-P-2354's accepted schema. Return the accepted typed immutable Settings value and precise validation/read errors.

## Details

Own only the ordinary file reader and focused author tests. Reuse existing read/parsing support where it fits and validate the supplied file against the admitted schema. Handle valid minimal and complete configurations, malformed TOML, missing required fields, unsupported legacy/unknown fields, invalid types and unavailable input with accurate results. The reader performs no Journal scan and exposes no history/currentness fields, protocol or gate. Do not require a Session, selected receiving admission, source-history lookup or a new public envelope. Existing Settings and callers are not migrated or rewritten.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git. Parallel workers own disjoint files; preserve unrelated changes. This Task does not authorize changes to existing Settings documents, existing callers, Journal or runtime. Keep Active until final integration.

### Definition of Done

Actual focused tests prove ordinary file reading/parsing, accepted typed immutable data, schema-valid results and precise schema/read failures with zero writes. Tests establish that no Journal/history/currentness protocol or gate is invoked or returned. Exact final implementation/source/test evidence and independent review establish this bounded path. Complete Configuration Read receiving integration, parent-wide and runtime completion remain separate.
