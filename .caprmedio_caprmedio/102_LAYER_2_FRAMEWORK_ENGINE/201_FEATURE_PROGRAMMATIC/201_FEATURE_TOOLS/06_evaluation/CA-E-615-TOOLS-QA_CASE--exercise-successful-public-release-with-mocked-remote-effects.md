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
version: 2
updated_at: "2026-10-10 12:49:55 +0400"
relations:
  evaluation_for: [CA-R-1925, CA-M-368]
---
# Summary

Exercise successful public release with mocked remote effects

## Scope

the successful path of one public release.

## Claim

**the Operator** **must** use a disposable end-to-end fixture with mocked remote effects and golden evidence to prove the initial gate, immutable push proof, actual new PR URL, changed public-document closure with unchanged D566 candidate snapshot, fresh non-promoting gate bridge, follow-up push, and same-PR refresh sequence.

## Details

The fixture proves the contract and ordering; it is not evidence that GitHub was written. It refuses a history-link follow-up that changes neither closure nor candidate, changes a candidate without a renewed local cycle, or uses the detached original reader as the renewed producer.
