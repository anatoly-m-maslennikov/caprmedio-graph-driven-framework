---
atom_id: "CA-D-613"
content_role: "Delivery"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Workflow bindings"
  depends_on: [Workflow, Step, Action, Tool]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  delivery_for: [CA-R-1922]
---
# Summary

Serialize public-release Workflow bindings

## Scope

the definition identities of one public-release execution.

## Claim

public-release execution **must** bind CA-O-188 and its CA-O-189 through CA-O-198 Step/Action definitions through the selected-run request manifest before native dispatch.

## Details

The sequence remains source-controlled Operations authority; executable code neither replaces nor derives definition revisions.
