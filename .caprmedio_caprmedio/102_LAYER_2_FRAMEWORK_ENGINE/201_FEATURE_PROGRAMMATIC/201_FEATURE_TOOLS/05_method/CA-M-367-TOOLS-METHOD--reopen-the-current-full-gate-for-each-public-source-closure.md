---
atom_id: "CA-M-367"
content_role: "Method"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Full Gate reuse"
  depends_on: [Full Gate, Source Proof, Test, Review]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  method_for: [CA-R-1924]
---
# Summary

Reopen the current Full Gate for each public source closure

## Scope

one gated public-source closure.

## Claim

**the Operator** **must** obtain and retain the existing typed FullGateEvidence for the exact selected source proof immediately before its public push, and repeat that gate after final Version History linking changes the snapshot.

## Details

The method consumes the current full-gate interface and durable receipt rather than reducing it to a boolean or recreating its test semantics.
