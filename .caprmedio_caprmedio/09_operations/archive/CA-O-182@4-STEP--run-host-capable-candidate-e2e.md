---
atom_id: CA-O-182@4
content_role: Operations
type: Step
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Release Version/Step: run host-capable Candidate E2E'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Test
  - Docker Image
  - Journal
version: 4
updated_at: 2026-10-24 00:38:25 +0400
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
