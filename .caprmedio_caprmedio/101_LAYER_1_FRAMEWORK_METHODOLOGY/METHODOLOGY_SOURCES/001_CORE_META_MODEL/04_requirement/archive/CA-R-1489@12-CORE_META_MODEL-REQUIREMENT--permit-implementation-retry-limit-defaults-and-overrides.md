---
version: 12
updated_at: 2026-10-24 00:38:25 +0400
relations:
  child_of:
  - CA-R-1488
subjects:
  governs: Implementation Retry Limit
  depends_on:
  - Implementation Retry Limit
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Property
atom_id: CA-R-1489@12
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Permit implementation retry-limit defaults and overrides

## Scope

effective Implementation Retry Limit selection for a Plan or Framework Instance Settings.

## Claim

an Implementation Retry Limit **must** take its effective value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** Framework Instance Settings.

- a Plan **may** have **<=1** explicit Implementation Retry Limit override, regardless of Label.
- an omitted override **must** preserve inheritance **without** copying the inherited value into that Plan.
- a retry decision **must** have **=1** valid effective limit; missing **or** ambiguous authority requires Operator disposition **before** another retry.

## Details
