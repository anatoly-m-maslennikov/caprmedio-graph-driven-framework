---
atom_id: "CA-E-610"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release request admission"
  depends_on: [Workflow, Operator Authorization, Tool]
version: 1
updated_at: "2026-10-10 19:05:35 +0400"
relations:
  evaluation_for: [CA-R-1920, CA-M-365]
---
# Summary

Validate public-release request admission

## Scope

one public-release request before execution.

## Claim

**the Operator** **must** verify that missing fields, unknown fields, bad digests, unsafe refs, malformed Run graph, stale preview, and absent or stale authorization all stop before a native binding is invoked.

## Details

Use a disposable Project and mock bindings. A valid preview alone is not execute success.
