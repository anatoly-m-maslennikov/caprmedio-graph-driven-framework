---
version: 20
updated_at: 2026-10-29 07:45:27 +0400
relations:
  child_of:
  - CA-R-1488
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan.implementation_retry_limit'
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.implementation.retry_limit
  - Entity/Object/Continuant/Actor/Operator
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Entity/Object/Continuant/Term//Property
atom_id: CA-R-1489@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 4
type: Rule
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

## Details
