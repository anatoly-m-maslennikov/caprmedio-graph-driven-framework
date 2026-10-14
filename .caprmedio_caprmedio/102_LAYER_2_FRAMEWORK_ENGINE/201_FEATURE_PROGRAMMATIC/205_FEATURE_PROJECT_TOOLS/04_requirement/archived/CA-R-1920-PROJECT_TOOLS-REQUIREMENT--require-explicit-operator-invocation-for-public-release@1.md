---
atom_id: "CA-R-1920"
content_role: "Requirement"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release invocation"
  depends_on: [Operator, Workflow, Action, Journal]
version: 1
updated_at: "2026-10-10 19:05:35 +0400"
relations:
  relates_to: [CA-O-188, CA-O-196, CA-M-365, CA-E-610, CA-D-610]
---
# Summary

Require explicit Operator invocation for public release

## Scope

one public-release Workflow invocation.

## Claim

**the Operator** **must** explicitly authorize the exact selected public-release request, definition manifest, source-currentness proof, effect set, and personal remote before a public commit, push, or PR effect begins.

## Details

Preview, preparation, and planning do not authorize execution. Missing, stale, or differently bound authorization stops before any remote effect.
