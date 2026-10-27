---
atom_id: CA-P-2356@7
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Settings
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Project.Settings
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 7
updated_at: 2026-10-24 10:27:10 +0400
relations:
  is_decomposition_of:
  - CA-P-2300
tier: 3
---
# Summary

Verify ordinary Settings file reader independently

## Objective

Independently verify CA-P-2354's aligned schema/source contract and CA-P-2355's ordinary standalone Settings file reader before final integration.

## Details

Own independent verification evidence and targeted tests only. Read the final schema, source description and implementation. Exercise actual ordinary file reads with independently authored expected values: valid minimal and complete schema documents, malformed TOML, missing required fields, unknown/legacy fields, wrong types and unavailable input. Verify the accepted typed immutable Settings value and accurate diagnostics. Explicitly test that the reader does not scan Journal or expose or gate on history/currentness. A Session, recorded Action, selected receiving route or history protocol is not a precondition for this ordinary file reader.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git. Parallel workers own disjoint files; preserve unrelated changes. This Task does not authorize changes to existing Settings documents, existing callers, Journal or runtime. Keep Active until final integration.

### Definition of Done

Independent actual positive/refusal checks pass on exact final code/source/test pins, with correct typed values, diagnostics and no writes. No Journal scan, history/currentness output or gate appears in the connected reader. Existing Settings/callers and Journal/runtime are not changed by this work, and unrelated pre-existing edits are preserved. Return exact executed checks and unresolved limits for final integration. Complete Configuration Read receiving integration, parent-wide and runtime completion remain separate.

### Completion checkpoint

Final independent acceptance against committed `de558c227` passed 18 ordinary-reader tests plus 14 genuine-Session Query and 12 existing Read-receiver regressions: 44 tests in 86.425 seconds. Checks establish complete typed immutable values, fresh exact document copies, missing/malformed/unknown/legacy/type/table/range refusals, original source/schema pin retention and stale-state refusal without effects. Actual source-observation spies prove malformed/unreadable/symlink Journal contents are never read; history/currentness fields and gates are absent. A Session remains unnecessary for ordinary Settings Read.

Reader/schema pins remained unchanged across the counted independent run. Root's fresh final connector regression passed 307 tests in 68.008 seconds. This is final integration acceptance of the narrow source-bound ordinary file reader, not live startup or complete Configuration Read receiving acceptance.

Reader `e136cbee6424c385d792be7e33e25e33ac8d4e9ec4221f052c21c87bb8357784`; pure schema `a4dc1b8e867468b02a34cae602b13593948e2d233bf152b6bc3f3bb79deee27e`; author tests `131ad22988437b8925986357baf4f5e7d2678636adfd4a82fc4623e26251977c`; independent reader tests `698a8f9f2407d60790213b38245387e7207cc7a20ef23ad600d3bf3fba8cbdb5`.

Independent Query regression file SHA-256: `b80846d3499e69d290525476aa13d6569c2755bf8b9eb753b9d2a8811f2ca193`. Source closure is the nine accepted Version/digest pins in `project_settings_schema.py::SCHEMA_PINS`, including D366 v10, E459 v19 and M284 v14. Existing Settings/callers and Journal/runtime are unchanged by this work; unrelated pre-existing edits remain untouched. P2300/P2280 receiving/caller integration and broader parent/runtime completion remain open.
