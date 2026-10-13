---
atom_id: CA-P-2298
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
  depends_on: [Atom, Scope Unit, Workflow, Configuration, Plan]
version: 2
updated_at: "2026-10-13 05:41:07 +0400"
relations:
  is_decomposition_of: [CA-P-2257]
---
# Summary

Preserve carrier bytes during property edits

## Objective

Prepare exact property edits against raw Atom carrier bytes, reusing existing YAML parsing/span helpers where they fit. Preserve unrelated frontmatter, body, comments and newline style; refuse ambiguous spans. Keep this transform pure and test scalar/list/full-set/no-op cases. Reading, writing and Workflow Version/time remain separate; this child does not publish.

## Details

Estimated own work: 15 minutes. Split larger work into bounded children before execution. Inherit the parent Task's accepted contracts, current-source checks and authority boundaries. Internal helpers are not newly admitted Tools. Keep parsing, reading, writing and CLI responsibilities separate. The integration owner controls Plans and Git; parallel implementation owns disjoint files only.

### Bounded remaining YAML forms

Independent checks found valid, unambiguous block-list boundary and trailing-comma append failures. Their bounded repair does not complete this Task: whole-Property removal from a flow mapping and unique multiline block-entry removal still hit unsupported-form shortcuts. No accepted contract limits these operations to narrower YAML layouts.

Continue through [CA-P-2305 — Support remaining unambiguous YAML property spans](01-CA-P-2298-TASK--preserve-carrier-bytes-during-property-edits/01-CA-P-2305-TASK--support-remaining-unambiguous-yaml-property-spans.md). The child is limited to 15 minutes; retain the full original Objective and independent acceptance gate. No public binding, publication or live migration is enabled by pure transform tests.

### Definition of Done

The Plan is not Done until exact implementation/source pins, focused positive/refusal/no-op checks and an independent review establish this child's bounded outcome. Preparation alone, invented public bindings, source-policy changes, deferred publication or live Core migration do not satisfy it. Parent-wide and runtime completion remain separate.
