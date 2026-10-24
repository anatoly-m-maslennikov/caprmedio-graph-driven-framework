---
atom_id: CA-R-1920
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Public release invocation
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/History/Journal
version: 7
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Require explicit Operator invocation for public release

## Scope

one public-release Workflow invocation.

## Claim

**the Operator** **must** explicitly authorize the exact selected public-release request, definition manifest, source-currentness proof, effect set, and personal remote before a public commit, push, or PR effect begins.

## Details

Preview, preparation, and planning do not authorize execution. Missing, stale, or differently bound authorization stops before any remote effect.
