---
atom_id: CA-P-2355@3
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
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Configuration
  - Plan
version: 3
updated_at: 2026-10-13 23:28:57 +0400
relations:
  is_decomposition_of:
  - CA-P-2300
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

### Completion checkpoint

Committed implementation `de558c227` keeps pure parsing/types in `project_settings_schema.py` and file I/O in `project_settings_reader.py`. It validates the complete admitted current Settings document, returns typed immutable values and retained physical/schema pins, preserves optional-field absence and exact supplied values, and refuses malformed, incomplete, unknown/legacy, unavailable, unsafe or stale sources without writes. Optional MCP port validation follows accepted D366 v10 with no default, fallback or activation.

Final author checks passed 8 tests in 5.862 seconds. Independent reader/Query/Read-receiver checks passed 44 tests in 86.425 seconds, including 18 ordinary-reader cases; Root's fresh connector regression passed 307 tests in 68.008 seconds. Actual source-observation spies and malformed/unsafe Journal fixtures prove no Journal scan/read; the snapshot exposes no history, logical Revision or currentness. Final code/source/test integration and independent review accept only this standalone ordinary file-read path.

Reader `e136cbee6424c385d792be7e33e25e33ac8d4e9ec4221f052c21c87bb8357784`; pure schema `a4dc1b8e867468b02a34cae602b13593948e2d233bf152b6bc3f3bb79deee27e`; author tests `131ad22988437b8925986357baf4f5e7d2678636adfd4a82fc4623e26251977c`; independent reader tests `698a8f9f2407d60790213b38245387e7207cc7a20ef23ad600d3bf3fba8cbdb5`.

The nine authority pins in `project_settings_schema.py::SCHEMA_PINS` include accepted D366 v10, E459 v19 and M284 v14. No existing Settings/caller migration or Journal/runtime change occurred. P2300/P2280 complete Configuration Read receiving integration, parent-wide completion and live runtime remain separate and open.
