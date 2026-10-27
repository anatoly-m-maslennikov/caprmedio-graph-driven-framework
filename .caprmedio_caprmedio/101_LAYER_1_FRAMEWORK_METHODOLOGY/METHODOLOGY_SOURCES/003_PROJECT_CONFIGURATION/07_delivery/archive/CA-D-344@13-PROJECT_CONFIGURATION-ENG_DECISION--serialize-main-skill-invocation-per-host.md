---
subjects:
  governs: Subject/Engineering/CAPRMEDIO Main Skill
  depends_on:
  - Subject/Engineering/CAPRMEDIO Main Skill
version: 13
updated_at: 2026-10-25 01:04:58 +0400
relations: {}
atom_id: CA-D-344@13
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Main Skill Invocation per Host

## Scope

Host Invocations for the CAPRMEDIO Main Skill **and** separately authorized compatibility layers.

## Claim

for the CAPRMEDIO Main Skill, the Host Invocation **must** serialize as `$ca` **in** Codex; **if** a Claude compatibility Extension **or** Operator-provided compatibility layer is separately authorized by the Operator, **then** its Host Invocation **must** serialize as `/ca` **in** Claude.

## Details
