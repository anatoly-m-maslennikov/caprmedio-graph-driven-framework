---
atom_id: CA-R-2267@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery/Type: Policy'
relations: {}
version: 2
updated_at: 2026-10-29 10:51:18 +0400
---
## Summary

Define Delivery Type Policy

## Claim

Policy is the Delivery Type for reusable rules governing how a declared kind of Object or property is represented, stored or delivered across its applicable cases. The rule may apply through the governed kind and its specializations rather than through named Scope Unit children. It is independent of numeric Tier. Its applicability conditions define the family of cases; a bounded representation choice uses Delivery Type Decision.

## Semantics

The recent Core representation-policy decision uses this reusable meaning. It does not add the Method Eng Policy actual-child ownership condition to every Delivery Policy. The source may be reusable Core authority even when its owning Core Meta-model Scope Unit has no child Scope Units.
