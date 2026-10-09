---
atom_id: "CA-E-615"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release successful execution"
  depends_on: [Git Commit, Pull Request, Full Gate, Tool]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  evaluation_for: [CA-R-1925, CA-M-368]
---
# Summary

Exercise successful public release with mocked remote effects

## Scope

the successful path of one public release.

## Claim

**the Operator** **must** use a disposable end-to-end fixture with mocked remote effects and golden evidence to prove the initial gate, immutable push proof, actual new PR URL, changed history snapshot, renewed gate, follow-up push, and same-PR refresh sequence.

## Details

The fixture proves the contract and ordering; it is not evidence that GitHub was written.
