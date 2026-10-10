---
atom_id: "CA-R-1924"
content_role: "Requirement"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release full gate"
  depends_on: [Full Gate, Source Proof, Test]
version: 3
updated_at: "2026-10-10 19:05:35 +0400"
relations:
  relates_to: [CA-O-193, CA-O-194, CA-O-198, CA-M-367, CA-E-614, CA-D-615]
---
# Summary

Require current typed Full Gate before public push

## Scope

one stable local-release candidate and its first public publication.

## Claim

the public-release Tool **must** run and retain fresh complete typed public Full Gate evidence for the stable local-release candidate and initial public-material closure before its first public effect. One Operator command authorizes the covered workflow and its Actions. Only the exact later PR-URL/concise-Version-History metadata follow-up may reopen that retained public gate without another suite, gate, review, or authorization.

## Details

The public gate derives its candidate identity from the current `RELEASE_VERSION` evidence but is a distinct public-suite result. A pass flag, hand-authored JSON, stale receipt, local-only gate, or evidence from another candidate or public closure is not sufficient. A changed executable candidate, Methodology, package, Version, or `version.toml` stops public effects until a new local candidate completes its full suite and same-bytes promotion and live verification, followed by a new public suite. Mechanical insertion of the actual PR URL into the already-generated short Version History summary may reopen only the same retained public Full Gate evidence; any substantive summary rewrite requires a new public suite.
