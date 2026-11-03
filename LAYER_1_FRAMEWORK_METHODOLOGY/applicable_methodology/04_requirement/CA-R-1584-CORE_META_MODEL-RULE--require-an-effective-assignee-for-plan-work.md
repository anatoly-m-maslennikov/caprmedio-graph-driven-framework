---
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee'
  passive:
  - Atom/(.Role := Plan)
  - Actor
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1584
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1584-CORE_META_MODEL-RULE--require-an-effective-assignee-for-plan-work.md
  source_atom_id: CA-R-1584
  source_atom_revision: 23
  source_sha256: 82d207882cc9220b1344d225b7343f91d35cfdbed775b63b23fd4493817a78f9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require an effective Assignee for Plan work

## Claim scope

Plan Atoms with their own work content, excluding pure Hubs **without** their own work.

## Claim

**every** Plan Atom with its own work content **must** have **`=1`** effective Assignee; a pure Hub **without** its own work does **not** require an additional Assignee merely because it organizes other Plans.
