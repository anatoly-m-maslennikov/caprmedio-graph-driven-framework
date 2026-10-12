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
  depends_on: [Full Gate, Source Proof, Test]
version: 2
updated_at: "2026-10-10 18:14:20 +0400"
relations:
  relates_to: [CA-O-193, CA-O-194, CA-O-198, CA-M-367, CA-E-614, CA-D-615]
---
# Summary

Require current typed Full Gate before public push

## Scope

one stable, tested local-release candidate used by a public release.

## Claim

the public-release Tool **must** reopen durable typed FullGateEvidence for the stable local-release candidate before public effects. One Operator command authorizes the covered workflow and its Actions; a PR URL or concise Version History metadata update alone does not require another suite, gate, review, or authorization.

## Details

The accepted interface is the current `RELEASE_VERSION` full-gate interface. A pass flag, hand-authored JSON, stale receipt, or evidence from another candidate is not sufficient. A changed executable candidate, Methodology, package, Version, or `version.toml` stops public effects until a new local candidate completes its full suite and same-bytes promotion and live verification. Mechanical insertion of the actual PR URL or short Version History summary leaves that tested candidate valid.
