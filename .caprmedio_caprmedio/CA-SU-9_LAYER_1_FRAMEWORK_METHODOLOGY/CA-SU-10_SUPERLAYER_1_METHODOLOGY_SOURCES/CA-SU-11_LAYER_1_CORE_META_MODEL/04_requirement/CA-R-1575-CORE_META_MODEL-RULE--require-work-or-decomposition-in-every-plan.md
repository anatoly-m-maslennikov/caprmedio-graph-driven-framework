---
atom_id: CA-R-1575
ref_id: CA-R-1575
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Atom.Content
tier: 2
status: Active
version: 27
updated_at: 2026-11-08 19:06:46 +0400
carrier_destination:
  file:
    name: CA-R-1575-CORE_META_MODEL-RULE--require-work-or-decomposition-in-every-plan.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Require work or decomposition in every Plan

## Claim

### Prose Claim


Plan Atoms other than Work Reports, their own work, and their direct Plan containment.


Every Plan Atom other than a Work Report **must** have **`>=1`** of:

- its own work content;
- **`>0`** outgoing derived `CONTAINS` links **to** directly contained Plan Atoms.

both contributions **may** be present within the same Claim; a Summary alone **without** either contribution is insufficient.
