---
atom_id: CA-R-1489
ref_id: CA-R-1489
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Plan).Implementation Retry Limit'
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Implementation Retry Limit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Plan)/(.Header.Form: Plan)'
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Term//Property
tier: 4
relations:
  child_of:
  - CA-R-1488@21
status: Active
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1489-CORE_META_MODEL-RULE--permit-implementation-retry-limit-defaults-and-overrides.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1489-CORE_META_MODEL-RULE--permit-implementation-retry-limit-defaults-and-overrides.md
  source_atom_id: CA-R-1489
  source_atom_revision: 25
  source_sha256: a1a7f0bd223749680fda44fc9b6b0556a7bd4899be89315e848f1f1e0108e7f8
  original_relations_sha256: fb00d26782cf16ed70925bcf37271a24fb7ade9de38397c303a37b222a73f23d
---
## Summary

Permit implementation retry-limit defaults and overrides

## Claim

### Prose Claim


effective Implementation Retry Limit selection for a Plan or Framework Instance Settings.


an Implementation Retry Limit **must** take its effective value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** Framework Instance Settings.

- a Plan **may** have **<=1** explicit Implementation Retry Limit override, regardless of Label.
- an omitted override **must** preserve inheritance **without** copying the inherited value into that Plan.
- a retry decision **must** have **=1** valid effective limit; missing **or** ambiguous authority requires Operator disposition **before** another retry.
