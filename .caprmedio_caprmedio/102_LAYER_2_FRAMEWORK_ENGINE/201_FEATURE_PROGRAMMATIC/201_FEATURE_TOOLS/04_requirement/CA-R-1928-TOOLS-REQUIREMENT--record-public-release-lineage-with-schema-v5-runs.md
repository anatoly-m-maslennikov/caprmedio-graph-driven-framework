---
atom_id: "CA-R-1928"
content_role: "Requirement"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Journal lineage"
  depends_on: [Journal, Workflow, Step, Action, Tool Call]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  relates_to: [CA-O-188, CA-M-369, CA-E-618, CA-D-618]
---
# Summary

Record public-release lineage with schema-v5 Runs

## Scope

the Journal evidence of one public-release execution.

## Claim

**the Operator** **must** record actual Workflow, Step, and Action Runs with schema-v5 parentage and attach each Tool-call input, result, effect, and report reference to its parent Step and Action evidence.

## Details

This Claim introduces no Tool Run type and no independent Journal schema. Preview, rejection, or absent recording evidence does not manufacture a Run or a successful public effect.
