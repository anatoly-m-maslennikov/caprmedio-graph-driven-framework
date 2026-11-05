---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Project
version: 3
updated_at: 2026-11-04 09:19:08 +0400
atom_id: CA-R-2424
ref_id: CA-R-2424
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2424-CORE_META_MODEL-RULE--define-local-scope-contract-tier-zero.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define local Scope Contract Tier Zero

## Claim

### Prose Claim


Local foundational commitments of Scope Units.


A Scope Unit’s local foundational commitments are expressed by its Atoms at numeric Tier `0`, whose readable Tier Label is Scope Contract. Tier `0` applies to Project and non-Project Scope Units. Each Atom retains its Content Role and Type, including existing Operations Types such as Workflow, Action and Step. Tier `1` and above specializes or realizes the local foundational commitments. This rule does not require an Atom for every Content Role or exactly one Tier `0` Atom for a Scope Unit. An Atom of Form Goal whose active Subject resolves to the Project Scope Unit root carries Tier `-1` under CA-R-2132.
