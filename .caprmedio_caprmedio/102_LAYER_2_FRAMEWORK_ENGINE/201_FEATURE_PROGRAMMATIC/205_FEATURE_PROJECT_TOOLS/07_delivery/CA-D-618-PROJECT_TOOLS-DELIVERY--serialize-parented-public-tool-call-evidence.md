---
atom_id: "CA-D-618"
content_role: "Delivery"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Tool-call Journal evidence"
  depends_on: [Journal, Workflow, Step, Action, Tool Call]
version: 1
updated_at: "2026-10-10 19:05:35 +0400"
relations:
  delivery_for: [CA-R-1928]
---
# Summary

Serialize parented public Tool-call evidence

## Scope

Tool-call evidence of one public-release Action.

## Claim

public-release Tool-call evidence **must** serialize input, result, effect, and report references under the actual parent Step and Action Run records of the existing schema-v5 Journal.

## Details

This Delivery adds neither a Tool Run kind nor a new Journal event schema. Started, terminal, and recording-pending states remain the shared schema meanings.
