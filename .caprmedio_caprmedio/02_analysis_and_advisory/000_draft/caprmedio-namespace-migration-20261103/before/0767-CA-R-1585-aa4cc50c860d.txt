---
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee'
  passive:
  - Atom/(.Role := Plan)
  - Entity/Object/Continuant/Actor/AI Agent
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1585
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Default Plan work assignment to an AI Agent

## Claim scope

a Plan Atom with its own work and no explicit Assignee.

## Claim

**if** a Plan Atom has its own work **and** no explicit Assignee, **then** its effective Assignee **must** be **=1** AI Agent selected **to** execute that work.
