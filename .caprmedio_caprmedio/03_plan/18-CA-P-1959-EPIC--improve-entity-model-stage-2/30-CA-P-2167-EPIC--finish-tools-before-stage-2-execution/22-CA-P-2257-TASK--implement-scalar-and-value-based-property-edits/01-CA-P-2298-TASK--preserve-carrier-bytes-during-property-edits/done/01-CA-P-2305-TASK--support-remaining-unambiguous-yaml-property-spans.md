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
status: Done
subjects:
  governs: Tool
  depends_on: [Atom, Property, Plan]
version: 3
updated_at: "2026-10-13 06:06:15 +0400"
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

### Earlier remaining bounded work

The first implementation period repaired the flow-map, multiline-value and comment-loss cases, but independent checks still reproduce one valid failure: a list indicator on the line before its value. At that checkpoint this Task remained Active and kept its full Objective.

Completed through [CA-P-2306 — Resolve separate-line YAML list indicators](../01-CA-P-2305-TASK--support-remaining-unambiguous-yaml-property-spans/done/01-CA-P-2306-TASK--resolve-separate-line-yaml-list-indicators.md) before closure. The existing independent regression is failing evidence, not an accepted limitation.

### Completion receipt

The bounded pure-transform work is complete at code commit `f4f4c6ce6`. [Independent acceptance](../../../../../../_projection/core-entity-review/stage2/tools-first/property-carrier-acceptance.md) records actual prior-failure/final-pass evidence and exact source, code and test pins: 46 focused Property tests passed, and Root reran all 162 connector tests successfully. Required child Tasks are complete. Exact predecessor history is preserved.

This closes pure carrier preparation only. CA-P-2257 and CA-P-2167 remain Active; receiving bindings, Workflow metadata/history effects, publication, runtime, the pending FPF review and live migration retain their separate gates.

### Definition of Done

The Plan is not Done until independently authored exact-byte fixtures reproduce the defects on the prior code and pass on the final code; complete-value and complete-Atom checks still reject invalid or stale changes; unrelated bytes, comments and newline style are preserved; no-op remains exact; focused regressions and independent review pass at recorded pins. Safe refusals of required valid cases or preparation claims without the actual transform do not complete the Task. Parent-wide receiving/runtime/publication gates remain separate.
