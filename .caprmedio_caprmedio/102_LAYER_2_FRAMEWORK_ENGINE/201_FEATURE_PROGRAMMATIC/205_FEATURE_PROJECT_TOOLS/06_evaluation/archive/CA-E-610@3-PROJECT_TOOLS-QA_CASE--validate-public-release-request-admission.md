---
atom_id: CA-E-610@3
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Public Release/Request Admission
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Operator Authorization
  - Subject/Engineering/Public Release/Request Admission Evaluation
version: 3
updated_at: 2026-10-23 03:14:50 +0400
relations:
  evaluation_for:
  - CA-R-1920
  - CA-M-365
---
# Summary

Validate public-release request admission

## Scope

one public-release request before execution.

## Claim

**the Operator** **must** verify that missing fields, unknown fields, bad digests, unsafe refs, malformed Run graph, stale preview, and absent or stale authorization all stop before a native binding is invoked.

## Details

Use a disposable Project and mock bindings. A valid preview alone is not execute success.
