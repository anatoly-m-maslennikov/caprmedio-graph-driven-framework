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
