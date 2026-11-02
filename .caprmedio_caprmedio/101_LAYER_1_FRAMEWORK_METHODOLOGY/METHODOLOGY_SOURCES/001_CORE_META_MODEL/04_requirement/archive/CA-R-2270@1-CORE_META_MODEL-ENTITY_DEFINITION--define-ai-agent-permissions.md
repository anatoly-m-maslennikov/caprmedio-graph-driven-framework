---
atom_id: CA-R-2270@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Object/Continuant/Actor/AI Agent.Permissions
relations: {}
version: 1
updated_at: 2026-10-29 09:55:37 +0400
---
## Summary

Define AI Agent Permissions

## Claim

AI Agent Permissions groups the Operator-governed delegations, constraints and authorization rules applicable to an identified AI Agent. It has no standalone scalar value. The actual allowed actions, target Scopes, validity and revocation conditions remain in their governing permission sources under CA-R-846 and CA-R-852. The grouping grants no permission by itself and is not a new mandatory instance field.

### Formal claim

```text
Entity/Object/Continuant/Actor/AI Agent.Permissions{0}
```
