---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Interaction
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Interaction.Reporting Mode
  - Entity/Object/Continuant/Actor/Operator
version: 23
updated_at: 2026-10-29 10:13:48 +0400
relations:
  child_of:
  - CA-R-1402
atom_id: CA-R-1440@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Preserve mandatory information in every reporting mode

## Claim scope

mandatory information reported by **every** interaction reporting mode.

## Claim

**every** interaction reporting mode **must** report the following mandatory information:

- blockers **and** failed operations;
- ambiguity that requires Operator input;
- permission **or** approval requests;
- safety-critical information;
- material deviations from the requested outcome.
