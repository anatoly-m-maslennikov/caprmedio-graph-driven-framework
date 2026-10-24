---
atom_id: CA-E-610@4
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Public Release/Request Admission
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Operator Authorization
  - Subject/Engineering/Public Release/Request Admission Evaluation
version: 4
updated_at: 2026-10-24 00:38:25 +0400
relations:
  evaluation_for:
  - CA-R-1920
  - CA-M-365
tier: 3
---
# Summary

Validate public-release request admission

## Scope

one public-release request before execution.

## Claim

**the Operator** **must** verify that missing fields, unknown fields, bad digests, unsafe refs, malformed Run graph, stale preview, and absent or stale authorization all stop before a native binding is invoked.

## Details

Use a disposable Project and mock bindings. A valid preview alone is not execute success.
