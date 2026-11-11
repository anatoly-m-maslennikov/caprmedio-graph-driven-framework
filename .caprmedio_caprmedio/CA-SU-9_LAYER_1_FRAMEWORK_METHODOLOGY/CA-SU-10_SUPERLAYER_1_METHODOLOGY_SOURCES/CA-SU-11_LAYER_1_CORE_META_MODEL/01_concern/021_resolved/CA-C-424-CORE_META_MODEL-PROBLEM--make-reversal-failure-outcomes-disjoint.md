---
atom_id: CA-C-424
content_role: Concern
type: Problem
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: resolved
version: 5
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Approved Change Reversal/Outcomes
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
relations:
  concern_about:
  - CA-O-131
  - CA-P-1450
ref_id: CA-C-424
carrier_destination:
  file:
    name: CA-C-424-CORE_META_MODEL-PROBLEM--make-reversal-failure-outcomes-disjoint.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/01_concern/021_resolved
---
# Summary

Make reversal failure outcomes disjoint

## Concern

O131's failed and partial_failure predicates overlap for an uncertain first effect with zero confirmed effects.

## Evidences

Independent P1450 F1 read actual outcome rows: execution failure before any approved effect is confirmed matches failed, while uncertain completion matches partial_failure. O130 preserves the effect account but cannot make the Action's selected outcome deterministic.

## Blast radius

### Disposition

Done P1461 corrected O131v2's two outcome predicates. Independent P1463 passed known-zero, uncertain-zero and confirmed-partial cases and verified every other clause remained unchanged. This source overlap is resolved; no reversal execution is inferred.

P1461 makes known-zero-effect failure distinct from any uncertain/confirmed partial effect. Preserve current permission, history, references and Journal guards; re-review only changed outcome clauses. No runtime reversal was performed.
