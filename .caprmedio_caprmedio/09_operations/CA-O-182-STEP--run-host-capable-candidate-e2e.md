---
atom_id: CA-O-182
content_role: Operations
type: Step
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/caprmedio/Step//Release Version/Step: run host-capable Candidate E2E'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 10
updated_at: 2026-10-27 19:59:47 +0400
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-181
tier: 3
---
# Summary

Run host-capable Candidate E2E

## Step

This Step invokes CA-O-181 once after CA-O-186's immutable image canary, binding the exact candidate/package/image/N identity and explicit host-capable controller authorization.

## Details

Absent host capability is non-pass, not a fallback to the frozen Docker worker. Failed, partial, stale, unsafe or missing-recording results stop before Full Gate aggregation, promotion and retirement without replay.
