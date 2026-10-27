---
atom_id: CA-P-2269@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 34
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Action
  - Workflow
  - Configuration
  - Revision
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 5
updated_at: 2026-10-24 07:45:09 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
  blocks:
  - CA-P-2278
tier: 3
---
# Summary

Place rebuilt code and update exports and callers

## Objective

Rebuilt code placement and imports/callers match declared delivery bindings without losing legacy behavior.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Split concrete work larger than this bound into actual bounded children before execution. This Backlog Task is current pending work, not a future-Version Scope or authorization to execute now.

After accepted contracts and FPF review, inventory affected exports/callers and move only the approved rebuilt implementation into explicit CONNECTOR_TOOLS/TOOL_WORKFLOWS delivery bindings. Preserve unrelated legacy TOOLS and public imports/entry points deliberately; add focused compatibility checks. New authority folders alone do not relocate code or activate runtime capability.

Start only after CA-P-2251's actual accepted FPF review and independently accepted applicable current contracts, not a Plan-validation result or historical pins. Bind actual contract/API/code pins and permissions. Require separately accepted applicable Core alignment under CA-P-1970 where rules conflict; no Core/content work is included here. Source authoring or this pending Task grants no runtime/live authority.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Approved internal separation and evidence checks

Separate parsing, reading, writing and CLI code in each mixed module touched by the approved rebuild. Preserve the existing public connector API; helpers are internal modules, not separate Tools. Reuse fitting modules, with no umbrella facade or unrelated legacy cleanup. Keep lifecycle/Workflow policy outside connectors.

Before each move or extraction, resolve effective applicable authority (SG001), the canonical Tool binding of any CLI whose ownership would change (SG002), and the exact internal dependencies, imports, callers, exports and tests (SG003). For artifact_metadata.py, the proposed read-only helper split remains conditional until this bounded check identifies the exact cut and concrete need. Do not silently unify distinct parsing behavior. Preserve existing public entry points, validation, error handling and effect boundaries; report any concrete conflict before changing the agreed API or ownership.

### Definition of Done

The Plan is **not** Done if applicable accepted contracts/FPF gates or current pins are missing; focused valid, refusal and no-op/error/effect checks fail or lack actual results; unrelated behavior regresses; implementation is claimed from preparation; or deferred/unauthorized capability is enabled. Own work must not exceed 15 minutes without prior decomposition.
