---
atom_id: CA-R-1928@2
content_role: "Requirement"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: Archived
subjects:
  governs: "Public release Journal lineage"
  depends_on: [Journal, Workflow, Step, Action, Tool Call]
version: 2
updated_at: "2026-10-14 12:27:48 +0000"
relations: {}
---
# Summary

Record public-release lineage with schema-v5 Runs

## Scope

the Journal evidence of one public-release execution.

## Claim

**the Operator** **must** record actual Workflow, Step, and Action Runs with schema-v5 parentage and attach each Tool-call input, result, effect, and report reference to its parent Step and Action evidence.

## Details

This Claim introduces no Tool Run type and no independent Journal schema. Preview, rejection, or absent recording evidence does not manufacture a Run or a successful public effect.
