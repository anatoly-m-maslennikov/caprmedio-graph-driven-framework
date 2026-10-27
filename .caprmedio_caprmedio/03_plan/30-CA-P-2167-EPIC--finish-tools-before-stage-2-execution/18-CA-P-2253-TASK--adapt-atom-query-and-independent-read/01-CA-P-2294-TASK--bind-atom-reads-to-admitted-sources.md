---
atom_id: CA-P-2294
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/Workflow
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 9
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2253
tier: 3
---
# Summary

Bind Atom reads to admitted sources

## Objective

Bind the pure Atom Query/Read mechanics to the existing receiving admission, explicit source view and actual authoritative source resolver. Preserve independent Read, full data and explicit filtering. Prove stale/denied/ambiguous/no-effect cases without activating a new runtime route.

## Details

Estimated own work: 15 minutes. Split larger work into bounded children before execution. Inherit the parent Task's accepted contracts, current-source checks and authority boundaries. Internal helpers are not newly admitted Tools. Keep parsing, reading, writing and CLI responsibilities separate. The integration owner controls Plans and Git; parallel implementation owns disjoint files only.

### Remaining receiving connection

The bounded private dispatcher and its independent fixture review are complete. This is not connected runtime readiness. Continue the concrete receiving connection in [CA-P-2301 — Bind selected Read receivers](01-CA-P-2294-TASK--bind-atom-reads-to-admitted-sources/01-CA-P-2301-TASK--bind-selected-read-receivers.md).

### Definition of Done

The Plan is not Done until exact implementation/source pins, focused positive/refusal/no-op checks and an independent review establish this child's bounded outcome. Preparation alone, invented public bindings, source-policy changes, deferred publication or live Core migration do not satisfy it. Parent-wide and runtime completion remain separate.
