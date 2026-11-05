---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.AI Agent Confidence Threshold
version: 28
updated_at: 2026-11-05 13:55:01 +0400
relations:
  child_of:
  - CA-M-261
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-R-1559
status: Active
tier: 2
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-1559-CORE_META_MODEL-RULE--gate-governing-atom-changes-during-implementation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Gate governing Atom changes during implementation

## Claim

### Prose Claim

Changes to governing RMED Atoms during implementation.

Before a governing RMED Atom changes, resolve the effective Plan AI Agent Confidence Threshold under CA-R-2711, applicable permissions and additional Operator constraints. When confidence is below the threshold or an additional rule requires approval, request Operator disposition before changing the Atom. Autonomous change is allowed only when confidence meets the threshold and all applicable permissions and Operator constraints allow it. A prohibition remains a prohibition; confidence does not create permission.

An authorized RMED change establishes a new baseline under CA-M-262; resolve the affected work and Evaluations again against that baseline.
