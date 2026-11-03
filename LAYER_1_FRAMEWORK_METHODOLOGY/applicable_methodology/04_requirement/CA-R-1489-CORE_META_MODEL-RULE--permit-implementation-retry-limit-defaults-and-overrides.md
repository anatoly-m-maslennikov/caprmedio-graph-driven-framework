---
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-1488@21
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Plan).Implementation Retry Limit'
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Implementation Retry Limit
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Plan)/(.Type: Plan)'
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO <+ MODEL <+ Term//Property
atom_id: CA-R-1489
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1489-CORE_META_MODEL-RULE--permit-implementation-retry-limit-defaults-and-overrides.md
  source_atom_id: CA-R-1489
  source_atom_revision: 25
  source_sha256: ea5eae2d4e7f01a677deff37b1a7d04b80ba73a13d05a6240dc913c8018f5855
  original_relations_sha256: fb00d26782cf16ed70925bcf37271a24fb7ade9de38397c303a37b222a73f23d
---
## Summary

Permit implementation retry-limit defaults and overrides

## Claim scope

effective Implementation Retry Limit selection for a Plan or Framework Instance Settings.

## Claim

an Implementation Retry Limit **must** take its effective value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** Framework Instance Settings.

- a Plan **may** have **<=1** explicit Implementation Retry Limit override, regardless of Label.
- an omitted override **must** preserve inheritance **without** copying the inherited value into that Plan.
- a retry decision **must** have **=1** valid effective limit; missing **or** ambiguous authority requires Operator disposition **before** another retry.
