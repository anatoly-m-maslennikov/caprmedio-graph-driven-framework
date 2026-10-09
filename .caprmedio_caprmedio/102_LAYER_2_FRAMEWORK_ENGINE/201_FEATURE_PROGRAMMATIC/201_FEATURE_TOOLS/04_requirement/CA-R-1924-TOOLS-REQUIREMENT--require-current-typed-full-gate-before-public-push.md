---
atom_id: "CA-R-1924"
content_role: "Requirement"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release full gate"
  depends_on: [Full Gate, Source Proof, Test, Review]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  relates_to: [CA-O-193, CA-O-194, CA-O-198, CA-M-367, CA-E-614, CA-D-615]
---
# Summary

Require current typed Full Gate before public push

## Scope

the source snapshot immediately before each public push.

## Claim

**the Operator** **must** obtain current passed durable typed FullGateEvidence and integrated-review evidence for the exact public source snapshot before its initial or follow-up push.

## Details

The accepted interface is the current `RELEASE_VERSION` full-gate interface. A pass flag, hand-authored JSON, stale receipt, or evidence from another candidate is not sufficient.
