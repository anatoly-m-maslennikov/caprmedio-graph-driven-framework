---
atom_id: "CA-E-614"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Full Gate evidence"
  depends_on: [Full Gate, Source Proof, Test, Review]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  evaluation_for: [CA-R-1924, CA-M-367]
---
# Summary

Validate current typed public Full Gate

## Scope

one public push admission.

## Claim

**the Operator** **must** verify that only current passed typed `RELEASE_VERSION` FullGateEvidence with an exact candidate snapshot and durable receipt admits a public push, while pass JSON, missing receipt, stale proof, or wrong snapshot stops it.

## Details

When Version History changes after PR creation, the case requires a distinct renewed gate before the follow-up push.
