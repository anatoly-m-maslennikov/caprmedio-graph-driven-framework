---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Journal
  passive:
  - CAPRMEDIO <+ MODEL <+ Event Record
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ History
  - CAPRMEDIO <+ MODEL <+ Actor
version: 37
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1644
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1644-CORE_META_MODEL-RULE--recover-work-journal-coverage-without-invention.md
  source_atom_id: CA-R-1644
  source_atom_revision: 37
  source_sha256: 4ae3758dcd3042f93250d4c5be6075317e8445c076a736c122562aa853ee1581
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Recover Work Journal coverage without invention

## Claim scope

recovered observations retained by a Journal.

## Claim

a Journal **may** retain an Event Record recovered from evidence **only** for facts established by **any** of:

- observed Carrier state;
- preserved history;
- Artifact movement;
- native targets;
- review records; **or**
- bounded session state.

the Journal **must** preserve unresolved Actor, time, intent, scope, **or** outcome as explicit uncertainty rather than fabricated history.
