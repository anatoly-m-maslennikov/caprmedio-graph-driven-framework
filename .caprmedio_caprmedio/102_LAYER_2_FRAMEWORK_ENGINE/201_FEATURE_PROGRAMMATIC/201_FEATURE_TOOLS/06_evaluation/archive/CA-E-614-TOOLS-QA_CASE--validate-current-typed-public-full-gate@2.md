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
version: 2
updated_at: "2026-10-10 12:56:30 +0400"
relations:
  evaluation_for: [CA-R-1924, CA-M-367]
---
# Summary

Validate current typed public Full Gate

## Scope

one public push admission.

## Claim

**the Operator** **must** verify that only current passed typed `RELEASE_VERSION` FullGateEvidence with an exact D566 candidate snapshot, durable receipt, and exact public-document closure admits a public push, while pass JSON, missing receipt, stale proof, stale closure bridge, or wrong snapshot stops it.

## Details

The case requires a fresh non-promoting producer receipt and canonical CA-D-615 bridge for the initial O194 public-document closure before its first push. When Version History changes after PR creation, it requires a distinct fresh producer receipt and bridge for the changed O198 closure before the follow-up push. It proves that the selected N+1 same-Version package identity is reopened for both phases, while an original detached reader, stale receipt, caller-supplied bridge field, or synthesized closure bridge is refused.
