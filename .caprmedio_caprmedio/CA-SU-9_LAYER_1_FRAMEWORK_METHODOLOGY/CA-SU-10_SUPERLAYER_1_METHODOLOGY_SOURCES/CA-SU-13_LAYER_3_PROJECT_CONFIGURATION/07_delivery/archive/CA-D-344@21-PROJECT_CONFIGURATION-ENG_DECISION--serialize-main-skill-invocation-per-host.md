---
subjects:
  active: Entity/Aspect/UX/Entry
  passive:
  - Entity/Aspect/UX/Entry
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-344@21
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Main Skill Invocation per Host

## Claim scope

Host Invocations for the CAPRMEDIO Main Skill **and** separately authorized compatibility layers.

## Claim

for the CAPRMEDIO Main Skill, the Host Invocation **must** serialize as `$ca` **in** Codex; **if** a Claude compatibility Extension **or** Operator-provided compatibility layer is separately authorized by the Operator, **then** its Host Invocation **must** serialize as `/ca` **in** Claude.
