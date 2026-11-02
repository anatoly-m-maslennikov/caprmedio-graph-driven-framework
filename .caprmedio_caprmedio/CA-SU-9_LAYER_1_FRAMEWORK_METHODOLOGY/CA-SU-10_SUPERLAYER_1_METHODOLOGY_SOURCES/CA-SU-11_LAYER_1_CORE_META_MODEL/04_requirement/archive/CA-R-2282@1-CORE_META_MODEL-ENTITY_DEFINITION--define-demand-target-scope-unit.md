---
atom_id: CA-R-2282@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Demand Target Scope Unit

## Claim scope

The Claim Target Scope Unit property of a Demand Atom.

## Claim

Demand.Target Scope Unit **means** the resolved Claim Target Scope Unit carried by a Demand Atom; it identifies the Producer Scope Unit whose results that Demand constrains. When carried, it is the explicit top-level YAML string `claim_target_scope_unit` and resolves to one registered Scope Unit. It is not Claim Scope, another Local Scope Unit, or a value inferred from a Carrier location. A complete Current Demand Carrier follows the applicable resolution and carrying rules.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit[string]{0..1}
```
