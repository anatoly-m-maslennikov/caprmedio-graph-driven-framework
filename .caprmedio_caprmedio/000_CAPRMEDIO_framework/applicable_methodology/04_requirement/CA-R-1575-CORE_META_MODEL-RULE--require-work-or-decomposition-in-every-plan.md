---
atom_id: CA-R-1575
ref_id: CA-R-1575
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1575-CORE_META_MODEL-RULE--require-work-or-decomposition-in-every-plan.md
  source_atom_id: CA-R-1575
  source_atom_revision: 27
  source_sha256: 2981385ec61881264b8f18e7d363cdf8ff085dc35e2e9d0f02f54ad877714a72
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
