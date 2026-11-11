---
atom_id: "CA-M-367"
content_role: "Method"
current_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Full Gate reuse"
  depends_on: [Full Gate, Source Proof, Test, Tool, Operator, Version History]
version: 6
updated_at: "2026-10-10 19:05:35 +0400"
relations:
  method_for: [CA-R-1924]
---
# Summary

Reopen the current Full Gate for each public source closure

## Scope

one stable local-release candidate, its initial public closure, and an exact URL/history-only follow-up.

## Claim

the PUBLIC_RELEASE Tool **must** run and retain one fresh complete typed Public Full Gate for the stable selected local-release candidate and initial public closure before its first public effect. A later exact PR-URL/concise-Version-History metadata update reopens that public gate and does not invoke another suite, gate, review, package installation, or authorization when the candidate and all non-metadata bindings remain unchanged.

## Details

1. Before the public suite, reopen the original retained native package proof. Legacy `FullGateEvidence` uses its bound reader; native `NativeFullGateEvidence` uses the detached retained-packet reader. Both branches establish the immutable D566 candidate snapshot, framework version, version-carrier identity, selected N+1 package provenance, and completed local-suite evidence. That local evidence is an input, not the Public Full Gate.
2. The fresh public suite runs every declared public-suite test once against the fixed initial public closure and candidate. It retains typed Public Full Gate evidence with its actual reports and closure/candidate bindings. A boolean, copied test summary, local-only gate, or unverified digest is not public gate evidence.
3. The Tool derives every public-material closure locally and reopens its carriers before the corresponding public effect. The initial publication requires the fresh Public Full Gate. After the remote returns an actual matching PR URL, the exact URL/history-only follow-up proves that no executable candidate, Methodology, package, Version, `version.toml`, or other material changed, then reopens the same Public Full Gate.
4. A changed executable candidate, Methodology, package, Version, `version.toml`, or initial public-material closure requires a new local candidate where applicable, complete local suite, same-bytes promotion and live verification, followed by a new public suite. Earlier evidence never authorizes that changed release.
5. These checks run only within the exact Operator-commanded public-release workflow. Retaining or reopening evidence alone does not invoke public release.
