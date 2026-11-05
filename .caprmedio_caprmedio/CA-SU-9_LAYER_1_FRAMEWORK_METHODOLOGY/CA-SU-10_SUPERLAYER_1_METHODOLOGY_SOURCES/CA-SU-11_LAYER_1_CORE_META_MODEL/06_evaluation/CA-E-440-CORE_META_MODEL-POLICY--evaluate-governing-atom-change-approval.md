---
version: 38
updated_at: 2026-11-05 13:55:01 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-R-1559
  - CA-R-1591
  - CA-R-1552
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.AI Agent Confidence Threshold
atom_id: CA-E-440
status: Active
tier: 4
role: Evaluation
form: Eval Policy
carrier_destination:
  file:
    name: CA-E-440-CORE_META_MODEL-POLICY--evaluate-governing-atom-change-approval.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
---
## Summary

Evaluate governing Atom change approval

## Claim

### Prose Claim

Governing Atom changes.

The governing-Atom change Evaluation must fail if a change proceeds below the effective Plan AI Agent Confidence Threshold without Operator disposition, bypasses an applicable permission or Operator constraint, or proceeds without approval required by an additional rule. Meeting the threshold does not override a prohibition or create permission.

The Evaluation must also fail if an authorized RMED change is reported against the old unchanged baseline, or its affected work and Evaluations are not resolved again against the new baseline.
