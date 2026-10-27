---
atom_id: CA-P-2306@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Term//Property
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 06:12:23 +0400
relations:
  is_decomposition_of:
  - CA-P-2305
tier: 3
---
# Summary

Resolve separate-line YAML list indicators

## Objective

Unique-value block-list removal resolves the actual YAML entry indicator even when its value starts on another line, preserving unrelated bytes and comments.

## Details

Estimated own work: 10 minutes, maximum 15 before further decomposition. Reuse the existing YAML BlockEntryToken and node spans in the pure property carrier helper. Preserve comments between indicator and value, retained entries, LF/CRLF, and complete-result validation. Test the existing separate-line failing case and a commented indicator/value gap without adding a parser, public request fields or storage effects.

Inherit CA-P-2305's accepted contracts, source checks and different-reviewer requirement. Root owns Plans and Git. This is the remaining pure-transform defect, not receiving admission, metadata/history materialization, publication or live migration.

### Completion receipt

The bounded pure-transform work is complete at code commit `f4f4c6ce6`. [Independent acceptance](../../../../../../_projection/core-entity-review/stage2/tools-first/property-carrier-acceptance.md) records actual prior-failure/final-pass evidence and exact source, code and test pins: 46 focused Property tests passed, and Root reran all 162 connector tests successfully. Required child Tasks are complete. Exact predecessor history is preserved.

This closes pure carrier preparation only. CA-P-2257 and CA-P-2167 remain Active; receiving bindings, Workflow metadata/history effects, publication, runtime, the pending FPF review and live migration retain their separate gates.

### Definition of Done

The Plan is not Done until the independent separate-line regression is red on the prior implementation and green on the final exact pin; indicator/value comments and unrelated bytes survive; all focused property regressions pass; and a different reviewer accepts the bounded implementation. Parent Tasks retain their full requirements and independent closure checks.
