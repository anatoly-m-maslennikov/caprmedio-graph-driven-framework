---
atom_id: CA-C-436
ref_id: CA-C-436
container:
  scope_unit: CA-SU-16
role: Concern
form: Problem
topics:
  main_subject: Journal snapshot continuation integrity
  dependencies:
  - Subject/Domain/Node/Continuant/History/Journal
  - Event
  - Pagination
relations:
  relates_to: [CA-R-1866, CA-M-334, CA-M-336, CA-E-577]
status: resolved
version: 2
updated_at: 2026-10-23 03:14:50 +0400
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
---
# Summary

Reject captured-prefix mutation on continuation

## Disposition

Resolved in the Journal source contract: continuation revalidates source and
captured-member hashes, rejects changed/deleted/unreadable/truncated captured
data, and permits bytes appended after the sealed prefix.
