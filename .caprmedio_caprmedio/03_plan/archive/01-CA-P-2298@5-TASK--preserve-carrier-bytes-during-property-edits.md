---
atom_id: CA-P-2298@5
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
  - Atom
  - Scope Unit
  - Workflow
  - Configuration
  - Plan
version: 5
updated_at: 2026-10-24 06:04:19 +0400
relations:
  is_decomposition_of:
  - CA-P-2257
tier: 3
---
# Summary

Preserve carrier bytes during property edits

## Objective

Prepare exact property edits against raw Atom carrier bytes, reusing existing YAML parsing/span helpers where they fit. Preserve unrelated frontmatter, body, comments and newline style; refuse ambiguous spans. Keep this transform pure and test scalar/list/full-set/no-op cases. Reading, writing and Workflow Version/time remain separate; this child does not publish.

## Details

Estimated own work: 15 minutes. Split larger work into bounded children before execution. Inherit the parent Task's accepted contracts, current-source checks and authority boundaries. Internal helpers are not newly admitted Tools. Keep parsing, reading, writing and CLI responsibilities separate. The integration owner controls Plans and Git; parallel implementation owns disjoint files only.

### Earlier remaining YAML forms

Independent checks found valid, unambiguous block-list boundary and trailing-comma append failures. Their bounded repair does not complete this Task: whole-Property removal from a flow mapping and unique multiline block-entry removal still hit unsupported-form shortcuts. No accepted contract limits these operations to narrower YAML layouts.

Completed through [CA-P-2305 — Support remaining unambiguous YAML property spans](../01-CA-P-2298@5-TASK--preserve-carrier-bytes-during-property-edits/done/01-CA-P-2305-TASK--support-remaining-unambiguous-yaml-property-spans.md). The child is limited to 15 minutes; retain the full original Objective and independent acceptance gate. No public binding, publication or live migration is enabled by pure transform tests.

### Completion receipt

The bounded pure-transform work is complete at code commit `f4f4c6ce6`. [Independent acceptance](../../../../_projection/core-entity-review/stage2/tools-first/property-carrier-acceptance.md) records actual prior-failure/final-pass evidence and exact source, code and test pins: 46 focused Property tests passed, and Root reran all 162 connector tests successfully. Required child Tasks are complete. Exact predecessor history is preserved.

This closes pure carrier preparation only. CA-P-2257 and CA-P-2167 remain Active; receiving bindings, Workflow metadata/history effects, publication, runtime, the pending FPF review and live migration retain their separate gates.

### Definition of Done

The Plan is not Done until exact implementation/source pins, focused positive/refusal/no-op checks and an independent review establish this child's bounded outcome. Preparation alone, invented public bindings, source-policy changes, deferred publication or live Core migration do not satisfy it. Parent-wide and runtime completion remain separate.
