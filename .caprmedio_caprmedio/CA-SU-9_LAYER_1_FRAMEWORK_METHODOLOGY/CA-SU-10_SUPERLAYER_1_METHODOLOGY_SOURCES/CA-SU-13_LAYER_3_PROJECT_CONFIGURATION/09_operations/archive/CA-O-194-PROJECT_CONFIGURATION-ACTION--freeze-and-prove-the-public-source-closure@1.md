---
atom_id: "CA-O-194"
content_role: Operations
type: Action
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Freeze and prove public source closure"
  depends_on: [Full Gate, Source Proof, Tool Call, Journal]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  relates_to: [CA-O-188, CA-O-193, CA-R-1922, CA-R-1924, CA-R-1928]
---
# Summary

Freeze and prove the public source closure

## Action

Freeze and prove the public source closure **means** the native binding of one selected source proof to current passed `RELEASE_VERSION` Full Gate evidence and integrated review evidence.

## Details

The Action admits only the existing typed FullGateEvidence interface with a durable receipt bound to the exact candidate snapshot. It does not substitute arbitrary pass JSON, write a remote, or create a PR.
