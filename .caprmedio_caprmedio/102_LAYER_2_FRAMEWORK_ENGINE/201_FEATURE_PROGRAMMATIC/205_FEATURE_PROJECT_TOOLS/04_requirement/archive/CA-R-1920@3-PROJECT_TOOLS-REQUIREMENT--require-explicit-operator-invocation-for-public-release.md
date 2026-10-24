---
atom_id: CA-R-1920@3
content_role: "Requirement"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: Archived
subjects:
  governs: Public release invocation
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Workflow
  - Action
  - Journal
version: 3
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
---
# Summary

Require explicit Operator invocation for public release

## Scope

one public-release Workflow invocation.

## Claim

**the Operator** **must** explicitly authorize the exact selected public-release request, definition manifest, source-currentness proof, effect set, and personal remote before a public commit, push, or PR effect begins.

## Details

Preview, preparation, and planning do not authorize execution. Missing, stale, or differently bound authorization stops before any remote effect.
