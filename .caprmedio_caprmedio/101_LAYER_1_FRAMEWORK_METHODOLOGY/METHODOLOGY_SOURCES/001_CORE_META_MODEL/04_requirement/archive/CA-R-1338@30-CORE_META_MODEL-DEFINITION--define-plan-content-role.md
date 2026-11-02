---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Entity/Object/Continuant/Governing Objects/Atom.Content
version: 30
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1338@30
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Plan Content Role

## Claim scope

Atom Claims that state bounded intended work **or** intended outcomes under the common Plan model.

## Claim

An explicit Assignee, Autonomous Confidence Threshold or Implementation Retry Limit is an optional local override. Absence preserves the applicable inherited/default value rather than storing a duplicate. Existing rules require an effective Assignee for owned work and an effective threshold for autonomous execution; these counts describe the local overrides.

Plan **means** the Content Role of an Atom Claim that states bounded intended work **or** an intended outcome under the common Plan model; it does **not** define a reusable Workflow **or** an Actor participation/authorization policy.

A Plan may have zero or more distinct BLOCKS targets and zero or more incoming blockers. All blockers must be Done before blocked work starts. Endpoints are Current Plan Atoms, whose Status can be any admitted Current Plan Status; “Current” does not mean the single Status value Active. Cross-graph references retain their source identity and follow applicable endpoint constraints rather than becoming native Plan Graph nodes.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee[string]{0..1}
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Autonomous Confidence Threshold[int]{0..1}
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Implementation Retry Limit[int]{0..1}
```
