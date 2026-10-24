---
atom_id: CA-P-2305
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Property, Plan]
version: 1
updated_at: "2026-10-13 05:41:07 +0400"
relations:
  is_decomposition_of: [CA-P-2298]
---
# Summary

Support remaining unambiguous YAML property spans

## Objective

Pure Property preparation supports admitted unambiguous flow-mapping Property edits and unique multiline block-list entry removal without changing unrelated carrier bytes.

## Details

Estimated own work: 15 minutes. Split larger work before further execution. Retain CA-P-2298's full outcome, accepted R1934/M374/D623/E628 contracts and complete-result validation. Reuse existing YAML token/node spans; do not add another parser, public request schema or dependency. Cover first/middle/last/sole flow-map removal, lawful trailing delimiters, folded/literal multiline scalar entries, comments and LF/CRLF. Refuse genuinely ambiguous or invalid inputs; unsupported syntax alone must not hide required valid cases.

The implementation owner edits only the pure property carrier helper and existing focused tests. A different reviewer owns independent regression fixtures and accepts exact final pins. Root owns Plans and Git. No storage writer, Version/time materialization, receiving admission, live Atom or migration effects belong here.

### Definition of Done

The Plan is not Done until independently authored exact-byte fixtures reproduce the defects on the prior code and pass on the final code; complete-value and complete-Atom checks still reject invalid or stale changes; unrelated bytes, comments and newline style are preserved; no-op remains exact; focused regressions and independent review pass at recorded pins. Safe refusals of required valid cases or preparation claims without the actual transform do not complete the Task. Parent-wide receiving/runtime/publication gates remain separate.
